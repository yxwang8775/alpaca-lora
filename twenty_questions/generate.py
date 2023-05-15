import copy
from typing import List, Tuple, Any
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import numpy as np
from transformers import AutoTokenizer, GenerationConfig
from transformers import GenerationConfig, LlamaForCausalLM, LlamaTokenizer
import copy
import re


class MyGenerator():
    def __init__(self, model, tokenizer):
        self.model = model
        self.tokenizer = tokenizer
        self.n_tokens = 1000
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    def generate(self, input_texts: List[str], num_samples: int = 1, max_length: int = 1024, max_new_tokens=30,
                  top_k=40, top_p=0.75, do_sample=False, temperature=0.1, num_beams=4, **kwargs) -> List[str]:
        inputs = self.tokenizer(input_texts, padding=True, return_tensors='pt', truncation=True)
        batch_size, seq_len = inputs['input_ids'].shape

        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        generation_config = GenerationConfig(
            temperature=temperature,
            top_p=top_p,
            num_return_sequences=num_samples,
            top_k=top_k,
            num_beams=num_beams,
            do_sample=do_sample,
            max_length=max_length,
            **kwargs,
        )

        output_ids = self.model.generate(**inputs, max_new_tokens=max_new_tokens, generation_config=generation_config)
        generated = self.tokenizer.batch_decode(output_ids)
        print(f'\ngenerated0=**********{generated}***********\n')
        output_ids = output_ids[:, seq_len:]
        generated = self.tokenizer.batch_decode(output_ids)
        print(f'generated=**********{generated}***********')
        return generated

    def generate_text(self, prompt, output_regex=None, eos_token=None):
        text = self.generate([prompt])[0]
        if eos_token is not None:
            text = text.split(eos_token)[0]
        if output_regex is not None:
            pattern = re.compile(output_regex)
            try:
                return re.findall(pattern, text)[0]
            except:
                return f'error with ********\n\n{text}\n\n**********\n'
        return text



def get_target_concepts():
    """return the list of concepts that will be communicated via twenty questions"""
    target_concepts = {}
    target_concepts["coarse objects"] = [
        "apple",
        "television",
        "dinosaur",
        "airplane",
        "house",
        "tree",
        "coat",
        "shoes",
        "car",
        "train",
        "shower",
        "frisbee",
        "cow",
    ]
    target_concepts["refined objects"] = [
        "cosmic crisp apple",
        "giganotosaurus",
        "siberian huskey",
        "glass micropipette",
    ]
    target_concepts["verbs"] = [
        "jog",
        "catch",
        "defenestrate",
        "eat",
        "apologize",
        "operate",
        "pretend",
    ]
    target_concepts["emotions"] = [
        "anger",
        "love",
        "hate",
        "contentment",
        "jealousy",
        "surprise",
        "disgust",
        "hopefulness",
    ]
    target_concepts["abstract concepts"] = [
        "global poverty",
        "phase transition",
        "positive sum game",
        "beauty",
        "representative democracy",
        "tall",
        "mauve",
        "perspicacious",
    ]
    return target_concepts


def build_instruction(template: str, components: dict):
    template = copy.deepcopy(template)
    for r in components.keys():
        template = template.replace(r, components[r])
    return template


def post_process(x:str, task_name=None):
    if task_name in ['high_low_game']:
        pattern = re.compile(r'\d+')
        try:
            return re.findall(pattern, x)[0]
        except:
            return f'error with ********\n\n{x}\n\n**********\n'
    if task_name in ['twenty_questions']:
        x=x.lower()
        p_yes=x.find('yes')
        p_no=x.find('no')
        if p_no<p_yes:
            if p_no==-1:
                return "Yes."
            else:
                return "No."
        if p_no>p_yes:
            if p_yes==-1:
                return "No."
            else:
                return "Yes."
        else:
            return f'error with ********\n\n{x}\n\n**********\n'

    return x.split('\n')[0]


shared_prefix = "Alice and Bob are playing a game of twenty questions with each other. Bob will ask a series of questions, and Alice will respond to each question with a 'Yes' or 'No', until Bob is able to guess the concept that Alice is thinking of. Bob will ask questions such as \"Is the concept a plant?\"\n\n"
shared_conversation_start = "This is Alice and Bob's conversation, starting with Bob's first question.\n"

def twenty_questions_generation(generator, target, shared_prefix, shared_conversation_start, max_questions=20, task_name=None):
    alice_prefix = f"The concept Alice is thinking of and wants to communicate to Bob is '{target}'.\n\n"
    bob_context = shared_prefix + shared_conversation_start
    alice_context = shared_prefix + alice_prefix + shared_conversation_start
    for round in range(1, max_questions + 1):
        # Bob asks a question
        bob_context += "\nBob: "
        alice_context += "\nBob: "
        if round == 1:
            # help guide the conversation towards 20-questions-like questions
            bob_context += "Is the concept "
            alice_context += "Is the concept "
        print('\nbob generate\n')
        bob_response = generator.generate_text(bob_context, eos_token="?")+'?'
        # strip leading whitespace, and only keep one line of content
        bob_response = (bob_response.lstrip("\n ") + "\n").splitlines()[0]

        if round == 1:
            bob_response='an animal?'

        if target.lower() in bob_response.lower():
            # Bob figured it out!
            break

        # Alice answers Bob's questions with a "Yes" or "No"
        bob_context += bob_response + "\nAlice: "
        alice_context += bob_response + "\nAlice: "
        print('\nalice generate\n')
        alice_response=post_process(generator.generate_text(alice_context),task_name=task_name)
        if 'error' in alice_response:
            print(alice_response)
            return alice_response
        bob_context += alice_response
        alice_context += alice_response
        print(f'\n\nalice context={alice_context}\n\n')
        print(f'\n\nbob context={bob_context}\n\n')


model_name = '/nvme/wangyaoxiang/model/llama-7b-hf/snapshots/5f98eefcc80e437ef68d457ad7bf167c2c6a1348'
lora_weights = None


target = 13

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = LlamaForCausalLM.from_pretrained(model_name,
                                         load_in_8bit=False,
                                         # torch_dtype=torch.float16,
                                         device_map="auto",
                                         )

if lora_weights is not None:
    from peft import PeftModel

    model = PeftModel.from_pretrained(
        model,
        lora_weights,
        torch_dtype=torch.float16,
    ).to(DEVICE)

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

data = twenty_questions_generation(generator=generator,target='apple',shared_prefix=shared_prefix,
                                   shared_conversation_start=shared_conversation_start,task_name='twenty_questions')
print(f'data=*********************\n{data}')


# chat gpt apple:51 rounds