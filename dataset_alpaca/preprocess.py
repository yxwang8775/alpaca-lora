
import json
import os

import pandas as pd
from datasets import load_dataset, Dataset, load_from_disk
from tqdm import tqdm

# # Preprocess for commonsense_qa
# def pre_process(example):
#     for i in range(5):
#         example[chr(ord('A') + i)] = example['choices']['text'][i]
#     return example
#
# if task_name=='commonsense_qa':
#     dataset=dataset.map(pre_process).remove_columns(['question_concept', 'id', 'choices'])
from generate_data import get_dataset_args

task_name='cosmos_qa'
path, name, split = get_dataset_args(task_name)
dataset = load_dataset(path=path, name=name, split=split)
num=2
dataset = dataset.select(range(min(num, len(dataset))))

def preprocess(task_name,dataset):
    def squad(example):
        example['answer']=example['answers']['text'][0]
        return example
    def drop(example):
        example['context'] = example['passage']
        example['answer'] = example['answers_spans']['spans'][0]
        return example
    def cosmosqa(example):
        example['answer']=example[f'answer{example["label"]}']
        return example
    def definite_pronoun_resolution(example):
        example['answer']=example['candidates'][int(example['label'])]
        return example

    item = dataset.__getitem__(0)
    print(item)
    for i in item.keys():
        print(i)
        print(item[i])

    if task_name in ['squad','squad_v2']:
        dataset = dataset.map(squad).remove_columns(['id', 'title', 'answers'])
    if task_name in ['drop']:
        dataset = dataset.map(drop).remove_columns(['passage','answers_spans','query_id','section_id'])
    if task_name in ['cosmos_qa']:
        dataset = dataset.map(cosmosqa).remove_columns(['id', 'label', 'answer0','answer1','answer2','answer3'])
    if task_name in ['definite_pronoun_resolution']:
        dataset = dataset.map(definite_pronoun_resolution).remove_columns(['candidates','label'])

    item=dataset.__getitem__(0)
    print(item)
    for i in item.keys():
        print(i)
        print(item[i])
    return dataset

dataset=preprocess(task_name, dataset)
print(len(dataset))