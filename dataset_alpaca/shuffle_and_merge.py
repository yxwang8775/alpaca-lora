import json
import math
import random

data_all = []
prefix = 'alpaca23'
for task_name in ['mnli', 'wnli', 'snli',
                  'wic', 'aeslc', 'cnn_dailymail',
                  'gigaword', 'multi_news', 'samsum',
                  'xsum', 'squad',
                  'drop', 'cosmos_qa', 'ag_news', 'definite_pronoun_resolution',
                  'mrpc', 'qqp', 'imdb', 'paws', 'yelp_polarity',
                  'ai2_arc', 'anli', 'common_gen']:
    with open(f'./{prefix}/{task_name}.json', 'r') as f:
        data = json.load(f)
        data_all.extend(data)
random.shuffle(data_all)

with open(f'./{prefix}/{prefix}.json', 'w', encoding='utf-8') as f:
    json.dump(data_all, f, indent=4)



with open(f'./{prefix}/train.json', 'w', encoding='utf-8') as f:
    json.dump(data_all[0:math.floor(len(data_all) * 0.8)], f, indent=4)

with open(f'./{prefix}/valid.json', 'w', encoding='utf-8') as f:
    json.dump(data_all[math.floor(len(data_all) * 0.8):], f, indent=4)

#
# def json2txt(path, path2):
#     print(path)
#     print(path2)
#     with open(path, 'r', encoding='utf-8') as f:
#         data = json.load(f)
#         data = [d['text'] for d in data]
#         txt = '\n\n'.join(data)
#         with open(path2, 'w',encoding='utf-8') as f2:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
#             f2.write(txt)
#
#
# for name in [prefix, 'train', 'valid']:
#     json2txt(f'./{prefix}/{name}.json', f'./{prefix}/{name}.txt')
