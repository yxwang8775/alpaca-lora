import torch
import os
import sys
from typing import List

import fire
import torch
import transformers
from datasets import load_dataset, DatasetDict

print(f'cuda is {torch.cuda.is_available()}')

"""
Unused imports:
import torch.nn as nn
import bitsandbytes as bnb
"""

from peft import (
    LoraConfig,
    get_peft_model,
    get_peft_model_state_dict,
    prepare_model_for_int8_training,
    set_peft_model_state_dict,
)
from transformers import LlamaForCausalLM, LlamaTokenizer

from utils.prompter import Prompter
