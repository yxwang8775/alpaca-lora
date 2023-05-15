import copy
from typing import List, Tuple, Any
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import numpy as np
from transformers import AutoTokenizer, GenerationConfig
import copy
import re


class MyGenerator():
    def __init__(self, model, tokenizer):
        self.model = model
        self.tokenizer = tokenizer
        self.n_tokens = 1000
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    def generate(self, batch):
        tokenized_inputs = \
            self.tokenizer.batch_encode_plus(batch, truncation=True, max_length=self.n_tokens, return_tensors='pt',
                                             add_special_tokens=False, padding='longest').to(
                self.model.device)  # truncation
        res = self.model.generate(input_ids=tokenized_inputs.input_ids,
                                  attention_mask=tokenized_inputs.attention_mask,
                                  # eos_token_id=self.tokenizer.encode("\n")[0],  # prompt中是以\n表示结束
                                  pad_token_id=self.tokenizer.pad_token_id,
                                  max_new_tokens=30,
                                  do_sample=False)
        a = tokenized_inputs.attention_mask.shape[1]
        generated = self.tokenizer.batch_decode(res[:, a:], skip_special_tokens=True)
        return generated

    def generate2(self, input_texts: List[str], num_samples: int = 1, max_length: int = 1024, max_new_tokens=30,
                  top_k=0, top_p=0.9, do_sample=False, temperature=1.0, **kwargs) -> List[str]:
        inputs = self.tokenizer(input_texts, padding=True, return_tensors='pt', truncation=True)
        batch_size, seq_len = inputs['input_ids'].shape

        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        # if max_length is not None:
        #     if 't5' in self.model.config.model_type:
        #         max_length = min(self.tokenizer.model_max_length, max_length + seq_len)
        #     else:
        #         max_length = min(self.model.config.max_position_embeddings, max_length + seq_len)
        # if min_length is not None:
        #     if 't5' in self.model.config.model_type:
        #         min_length = min(self.tokenizer.model_max_length,min_length + seq_len)
        #     else:
        #         min_length = min(self.model.config.max_position_embeddings, min_length + seq_len)

        generation_config = GenerationConfig(
            temperature=temperature,
            top_p=top_p,
            num_return_sequences=num_samples,
            top_k=top_k,
            do_sample=do_sample,
            max_length=max_length,
            **kwargs,
        )
        print(generation_config)

        output_ids = self.model.generate(**inputs, max_new_tokens=max_new_tokens, generation_config=generation_config)
        output_ids = output_ids[:, seq_len:]
        return self.tokenizer.batch_decode(output_ids)


def build_instruction(template: str, components: dict):
    template = copy.deepcopy(template)
    for r in components.keys():
        print(f'template={template}')
        print(f'c[{r}]={components[r]}')
        template=template.replace(r, components[r])
        print(f'template={template}')
    return template


def post_process(x, task_name=None):
    if task_name in ['high_low_game']:
        pattern = re.compile(r'\d+')
        print(f'x={x}')
        return re.findall(pattern, x)[0]
    return x.split('\n')[0]


# 判断该加什么template
def select(prediction, target, task_name):
    if task_name == 'high_low_game':
        try:
            prediction = int(prediction)
            if prediction < target:
                return 0
            elif prediction > target:
                return 1
            else:
                return 2
        except:
            return 3
    return None



def multi_turn_generation(generator, template, components=None, max_depth=10, depth=0, task_name=None, target=None,
                          t_options=None, response_split=None):
    if components is None:
        components = {"instruction": "",
                      "input": "",
                      "output": ""}

    # 多轮任务只能batchsize=1
    template = copy.deepcopy(template)
    print(f'template={template}')
    text = build_instruction(template, components)
    print(f'text={text}')
    if response_split is not None:
        text += response_split
    generated = generator.generate2(input_texts=[text])
    print(f'generated={generated}')
    prediction = post_process(generated[0], task_name)
    print(f'predection={prediction}')

    components[f'G{depth}'] = prediction
    template += f'\n{{G{depth}}}'
    response = t_options[select(prediction=prediction, target=target, task_name=task_name)]
    if response is not None and depth <= max_depth:
        components[f'R{depth}'] = response
        template += f'\n{{R{depth}}}'
        return multi_turn_generation(generator=generator, template=template, components=components, max_depth=max_depth,
                                     depth=depth + 1, task_name=task_name, target=target, t_options=t_options,
                                     response_split=response_split)
    else:
        return build_instruction(template, components)


model_name = '/nvme/wangyaoxiang/model/llama-7b-hf/snapshots/5f98eefcc80e437ef68d457ad7bf167c2c6a1348'


components = {
    "{instruction}": "This is a conversation. Bob and Alice are playing a game. Alice have a number between 0 and 20."
                   " Bob has to guess it. Bob guess a number each time and then Alice will tell him that his guessing is"
                   " \"Too low\" or \"Too high\". Bob needs to consider the whole conversation history and guess the "
                     "number as soon as possible",
    "{input}": "Alice: Now I have a number between 0 and 20, You have to guess it. Just give me a number.\nBob:",
    "{output}": ""}

template = "Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.\n\n### Instruction:\n{instruction}\n\n### Input:\n{input}\n\n"
response_split = "### Response:\n"

# template = "{instruction}"

target = 13
t_options = ["Alice: Too low. Guess another number again.\nBob:",
             "Alice: Too high. Guess another number again.\nBob:",
             "Alice: Give a number, please\nBob:",
             None]

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = AutoModelForCausalLM.from_pretrained(model_name).to(DEVICE)
if 'llama' in model_name:
    from transformers import LlamaTokenizer

    tokenizer = LlamaTokenizer.from_pretrained(model_name)
else:
    tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token  # original pad token id is 50257, not in embedding matrix
tokenizer.pad_token_id = tokenizer.eos_token_id
model.config.pad_token_id = tokenizer.eos_token_id
# tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "left"
generator = MyGenerator(model=model, tokenizer=tokenizer)

data = multi_turn_generation(generator, template, components=components, max_depth=5, task_name='high_low_game',
                             target=13,
                             t_options=t_options, response_split=response_split)
print(f'data={data}')
