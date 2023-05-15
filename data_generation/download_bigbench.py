import json

from datasets import load_dataset

dataset=load_dataset("bigbench")

print(len(dataset))
print(dataset)
# print(dataset.__getitem__(0))
# data=[]
#
# for i in range(len(dataset)):
#     data.append(dataset.__getitem__(i))
#
# with open('./alpaca_cleaned.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, indent=4)