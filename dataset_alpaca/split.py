import json
import math
import random

prefix="alpaca_and_ecpsqr_2"
file=f"{prefix}/alpaca_and_ecpsqr_2.json"

with open(file, 'r') as f:
    data_all = json.load(f)
random.shuffle(data_all)

with open(f'./{prefix}/train.json', 'w', encoding='utf-8') as f:
    json.dump(data_all[0:math.floor(len(data_all) * 0.8)], f, indent=4)

with open(f'./{prefix}/valid.json', 'w', encoding='utf-8') as f:
    json.dump(data_all[math.floor(len(data_all) * 0.8):], f, indent=4)


def json2txt(path, path2):
    print(path)
    print(path2)
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        data = [d['text'] for d in data]
        txt = '\n\n'.join(data)
        with open(path2, 'w',encoding='utf-8') as f2:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f2.write(txt)


for name in ['train', 'valid']:
    json2txt(f'./{prefix}/{name}.json', f'./{prefix}/{name}.txt')
