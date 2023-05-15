from typing import List

import torch
import transformers
from peft import PeftModel
from transformers import GenerationConfig, AutoModelForCausalLM, AutoTokenizer
import re


class ModelWrapper():

    def __init__(self, model_name: str = "gpt2-xl", use_cuda: bool = True, checkpoint=None, lora_weights=None):
        """
        :param model_name: the name of the pretrained GPT2 model (default: "gpt2-xl")
        :param use_cuda: whether to use CUDA
        """
        print(f'modelname={model_name}')
        super().__init__()
        DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        print(f'device={DEVICE}')
        if checkpoint is not None:
            self._model = AutoModelForCausalLM.from_pretrained(checkpoint, device_map="auto")
        else:
            self._model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")
        print(f'modeldevice={self._model.device}')
        if lora_weights is not None:
            self._model = PeftModel.from_pretrained(
                self._model,
                lora_weights,
                torch_dtype=torch.float16,
            )

        print(f'lora={lora_weights}')
        if 'llama' in model_name:
            print(4)
            from transformers import LlamaTokenizer
            if checkpoint is not None:
                print(5)
                self._tokenizer = LlamaTokenizer.from_pretrained(checkpoint)
                print(6)
            else:
                print(7)
                self._tokenizer = LlamaTokenizer.from_pretrained(model_name)
        else:
            if checkpoint is not None:
                print(8)
                self._tokenizer = AutoTokenizer.from_pretrained(checkpoint)
            else:
                print(9)
                self._tokenizer = AutoTokenizer.from_pretrained(model_name)
        print(f'tokenizer={self._tokenizer}')
        self._tokenizer.pad_token = self._tokenizer.eos_token  # original pad token id is 50257, not in embedding matrix
        self._tokenizer.pad_token_id = self._tokenizer.eos_token_id
        self._model.config.pad_token_id = self._tokenizer.eos_token_id
        self._tokenizer.padding_side = "left"
        self.device = self._model.device
        print(f'device={self.device}')

    def generate(self, input_texts: List[str], num_samples: int = 1, max_length: int = 1024, max_new_tokens=30,
                 top_k=0, top_p=0.9, do_sample=False, temperature=1.0, **kwargs) -> List[str]:
        inputs = self._tokenizer(input_texts, padding=True, return_tensors='pt', truncation=True)
        batch_size, seq_len = inputs['input_ids'].shape
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        generation_config = GenerationConfig(
            temperature=temperature,
            top_p=top_p,
            num_return_sequences=num_samples,
            top_k=top_k,
            do_sample=do_sample,
            max_length=max_length,
            **kwargs,
        )
        output_ids = self._model.generate(**inputs, max_new_tokens=max_new_tokens, generation_config=generation_config)
        output_ids = output_ids[:, seq_len:]
        return self._tokenizer.batch_decode(output_ids)

    def generate_text(self, prompt, output_regex=None, eos_token='\n'):
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
