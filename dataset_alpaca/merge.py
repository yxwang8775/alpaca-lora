import json
import os
from os import listdir
import random
from datasets import load_dataset, Dataset, DatasetDict
import pandas as pd


def merge_json(file_list,output_file='data_all.json'):
    print(f'{file_list}')
    data_all=[]
    for file in file_list:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            data_all.extend(data)
    random.shuffle(data_all)
    print(f'{output_file}')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data_all, f, indent=4)
    ds=Dataset.from_pandas(pd.DataFrame(data=pd.read_json(output_file)))
    ds.to_json(f'dataset_{output_file}')
    # d = {'train': ds,
    #      }
    # dataset_dict=DatasetDict(d)
    # dataset_dict.to_json(f'dict_{output_file}')


file_list=["./alpaca_cleaned.json","./alpaca23/alpaca23.json"]
merge_json(file_list,"alpaca_gen.json")


