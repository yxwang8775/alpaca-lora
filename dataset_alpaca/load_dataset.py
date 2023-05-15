import json
import os

import pandas as pd
from datasets import load_dataset
from tqdm import tqdm

from template import PATTERNS, get_label_field


def get_dataset_args(task_name):
    # path name split
    data_path = {
        "rte": ["glue", "rte", 'train'],
        'mnli': ['glue', 'mnli', 'train'],
        "qnli": ["glue", "qnli", 'validation'],
        "wnli": ["glue", "wnli", 'validation'],
        'snli': ['snli', None, 'train'],
        "wic": ['super_glue', 'wic', 'validation'],
        'sst2': ["glue", 'sst2', 'validation'],
        'aeslc': ["aeslc", None, 'validation'],
        "cnn_dailymail": ['cnn_dailymail', '3.0.0', 'validation'],
        'gigaword': ['gigaword', None, 'validation'],
        "trec": ["trec", None, 'validation'],
        "multi_news": ['multi_news', None, 'validation'],
        "samsum": ['samsum', None, 'validation'],
        "xsum": ['xsum', None, 'validation'],
        "squad": ["squad", None, 'validation'],
        "squad_v2": ["squad_v2", None, 'validation'],
        "fix_punctuation": ["nbroad/fix_punctuation", None, 'validation'],
        "drop": ["drop", None, 'validation'],
        "cosmos_qa": ["cosmos_qa", None, 'validation'],
        "ag_news": ["ag_news", None, 'validation'],
        "definite_pronoun_resolution": ["definite_pronoun_resolution", None, 'validation'],
        'mrpc': ["glue", "mrpc", 'validation'],
        'qqp': ["glue", 'qqp', 'validation'],
        "imdb": ["imdb", None, 'validation'],
        "paws": ["paws", None, 'validation'],
        "yelp_polarity": ["yelp_polarity", None, 'validation'],
        "ai2_arc": ["ai2_arc", 'ARC-Easy', 'validation'],
        "anli": ["anli", None, 'dev-r1'],
        "common_gen": ["common_gen", None, 'validation'],
        'iwslt17zh': ["iwslt2017", 'iwslt2017-zh-en', 'validation'],
        "mtop": ["iohadrubin/mtop", 'mtop', 'validation'],

        "sst5": ["SetFit/sst5", None, 'validation'],

        "commonsense_qa": ["commonsense_qa", None, 'validation'],
        "copa": ['super_glue', 'copa', 'validation'],

        "boolq": ['super_glue', 'boolq', 'validation'],

    }
    return data_path[task_name]


data_path = {
    "rte": ["glue", "rte", 'train'],
    'mnli': ['glue', 'mnli', 'train'],
    "qnli": ["glue", "qnli", 'validation'],
    "wnli": ["glue", "wnli", 'validation'],
    'snli': ['snli', None, 'train'],
    "wic": ['super_glue', 'wic', 'validation'],
    'sst2': ["glue", 'sst2', 'validation'],
    'aeslc': ["aeslc", None, 'validation'],
    "cnn_dailymail": ['cnn_dailymail', '3.0.0', 'validation'],
    'gigaword': ['gigaword', None, 'validation'],
    "trec": ["trec", None, 'validation'],
    "multi_news": ['multi_news', None, 'validation'],
    "samsum": ['samsum', None, 'validation'],
    "xsum": ['xsum', None, 'validation'],
    "squad": ["squad", None, 'validation'],
    "squad_v2": ["squad_v2", None, 'validation'],
    "fix_punctuation": ["nbroad/fix_punctuation", None, 'validation'],
    "drop": ["drop", None, 'validation'],
    "cosmos_qa": ["cosmos_qa", None, 'validation'],
    "ag_news": ["ag_news", None, 'validation'],
    "definite_pronoun_resolution": ["definite_pronoun_resolution", None, 'validation'],
    'mrpc': ["glue", "mrpc", 'validation'],
    'qqp': ["glue", 'qqp', 'validation'],
    "imdb": ["imdb", None, 'validation'],
    "paws": ["paws", None, 'validation'],
    "yelp_polarity": ["yelp_polarity", None, 'validation'],
    "ai2_arc": ["ai2_arc", 'ARC-Easy', 'validation'],
    "anli": ["anli", None, 'dev-r1'],
    "common_gen": ["common_gen", None, 'validation'],
}
# begin=0
# for task_name in data_path.keys():
#     print(f'\'{task_name}\',',end='')
# for task_name in data_path.keys():
#     path, name, split = get_dataset_args(task_name)
#     if path=='gigaword':
#         begin=1
#     # if begin==0:
#     #     continue
#     print(f'{path},{name},{split}')
#     dataset = load_dataset(path=path, name=name, split=split)
# for task_name in ['qnli']:
#     path, name, split = get_dataset_args(task_name)
#     print(f'{path},{name},{split}')
#     dataset = load_dataset(path=path, name=name, split='train')
#     print(len(dataset))

dataset=load_dataset("nlpcloud/instructions-dataset-adapted-from-stanford-alpaca-for-gpt-j")
print(len(dataset['train']))
print(len(dataset['validation']))