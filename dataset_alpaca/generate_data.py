import copy
import json
import os
import random

import pandas as pd
from datasets import load_dataset
from tqdm import tqdm

from template import PATTERNS, get_label_field


def get_dataset_args(task_name):
    # path name split
    data_path = {
        "rte": ["glue", "rte", 'train'],
        'mnli': ['glue', 'mnli', 'train'],
        "qnli": ["glue", "qnli", 'train'],
        "wnli": ["glue", "wnli", 'train'],
        'snli': ['snli', None, 'train'],
        "wic": ['super_glue', 'wic', 'train'],
        'sst2': ["glue", 'sst2', 'train'],
        'aeslc': ["aeslc", None, 'train'],
        "cnn_dailymail": ['cnn_dailymail', '3.0.0', 'train'],
        'gigaword': ['gigaword', None, 'train'],
        "trec": ["trec", None, 'train'],
        "multi_news": ['multi_news', None, 'train'],
        "samsum": ['samsum', None, 'train'],
        "xsum": ['xsum', None, 'train'],
        "squad": ["squad", None, 'train'],
        "squad_v2": ["squad_v2", None, 'train'],
        "fix_punctuation": ["nbroad/fix_punctuation", None, 'train'],
        "drop": ["drop", None, 'train'],
        "cosmos_qa": ["cosmos_qa", None, 'train'],
        "ag_news": ["ag_news", None, 'train'],
        "definite_pronoun_resolution": ["definite_pronoun_resolution", None, 'train'],
        'mrpc': ["glue", "mrpc", 'train'],
        'qqp': ["glue", 'qqp', 'train'],
        "imdb": ["imdb", None, 'train'],
        "paws": ["paws", 'labeled_final', 'train'],
        "yelp_polarity": ["yelp_polarity", None, 'train'],
        "ai2_arc": ["ai2_arc", 'ARC-Easy', 'train'],
        "anli": ["anli", None, 'dev_r1'],
        "common_gen": ["common_gen", None, 'train'],
    }
    return data_path[task_name]


def preprocess(task_name, dataset):
    def squad(example):
        try:
            example['answer'] = example['answers']['text'][0]
        except:
            example['answer'] = 'I don\'t know.'
            print('no answer')
        return example

    def drop(example):
        example['context'] = example['passage']
        example['answer'] = example['answers_spans']['spans'][0]
        return example

    def cosmosqa(example):
        example['answer'] = example[f'answer{example["label"]}']
        return example

    def definite_pronoun_resolution(example):
        example['answer'] = example['candidates'][int(example['label'])]
        return example

    def common_gen(example):
        concepts = example['concepts']
        str = concepts[0]
        for j in range(len(concepts) - 1):
            str = str + ', ' + concepts[j]
        str = str + ' and ' + concepts[-1]
        example['concepts'] = str
        return example

    # def ai2arc(example):
    #     m={"A":0,"B":1,"C":2,"D":3}
    #     example

    item = dataset.__getitem__(0)
    print(item)
    for i in item.keys():
        print(i)
        print(item[i])

    if task_name in ['squad', 'squad_v2']:
        dataset = dataset.map(squad).remove_columns(['id', 'title', 'answers'])
    if task_name in ['drop']:
        dataset = dataset.map(drop).remove_columns(['passage', 'answers_spans', 'query_id', 'section_id'])
    if task_name in ['cosmos_qa']:
        dataset = dataset.map(cosmosqa).remove_columns(['id', 'label', 'answer0', 'answer1', 'answer2', 'answer3'])
    if task_name in ['definite_pronoun_resolution']:
        dataset = dataset.map(definite_pronoun_resolution).remove_columns(['candidates', 'label'])
    if task_name in ['common_gen']:
        dataset = dataset.map(common_gen)

    item = dataset.__getitem__(0)
    print(item)
    for i in item.keys():
        print(i)
        print(item[i])
    return dataset


def build_instructions(template, data: dict):
    text = template
    for key in data.keys():
        text = text.replace(f'{{{key}}}', str(data[key]))
    return text

def build_dict_instructions(template:dict, data: dict):
    new_t = copy.deepcopy(template)
    for k in template.keys():
        t=new_t[k]
        new_t[k] = build_instructions(t,data)
    return new_t



def generate_data(task_name, num, file=None, prefix=None,sum=None):
    pattern = PATTERNS[task_name]
    label_field = get_label_field(task_name)
    path, name, split = get_dataset_args(task_name)
    print(f'{path},{name},{split}')
    dataset = load_dataset(path=path, name=name, split=split)
    dataset = dataset.select(range(min(num, len(dataset))))
    dataset = preprocess(task_name, dataset)
    new_data = []
    for d in tqdm(dataset):
        if isinstance(pattern, dict):
            if d[label_field] < 0:
                print('label<0')
                continue
            templates = pattern[d[label_field]]
        else:
            templates = pattern

        template=templates[random.randint(0,len(templates)-1)]
        new_data.append(build_dict_instructions(template,d))

    random.shuffle(new_data)
    if sum is not None:
        new_data=new_data[:sum]
    js = new_data
    for d in js:
        d['task']=task_name

    if file is None:
        if prefix is None:
            file = f'./{task_name}.json'
        else:
            if not os.path.exists(f'./{prefix}'):
                os.mkdir(f'./{prefix}')
            file = f'./{prefix}/{task_name}.json'

    with open(file, 'w', encoding='utf-8') as f:
        json.dump(js, f, indent=4)


begin = 0

# for task_name in ['rte','mnli','qnli','wnli','snli',
#                   'wic','sst2','aeslc','cnn_dailymail',
#                   'gigaword','trec','multi_news','samsum',
#                   'xsum','squad','squad_v2',
#                   'drop','cosmos_qa','ag_news','definite_pronoun_resolution',
#                   'mrpc','qqp','imdb','paws','yelp_polarity',
#                   'ai2_arc','anli','common_gen']:
for task_name in ['mnli', 'wnli', 'snli',
                  'wic', 'aeslc', 'cnn_dailymail',
                  'gigaword', 'multi_news', 'samsum',
                  'xsum', 'squad',
                  'drop', 'cosmos_qa', 'ag_news', 'definite_pronoun_resolution',
                  'mrpc', 'qqp', 'imdb', 'paws', 'yelp_polarity',
                  'ai2_arc', 'anli', 'common_gen']:
    # if task_name == 'squad_v2':
    #     begin = 1
    # if begin == 0:
    #     continue
    print(f'generate {task_name}')
    num = 1000
    # num = 30000
    generate_data(task_name=task_name, num=num, prefix='alpaca23',sum=num)
