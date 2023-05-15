import json

path = 'alpaca/alpaca.txt'

with open(path, 'r', encoding='unicode_escape') as f:
    txt = f.read()
    # txt=txt.replace('\\n','\n')
    # txt = txt.replace('\\\n', '\n')
    #
    # txt = txt.replace('\\t', '\t')
    # txt = txt.replace('\\\"', '\"')
    # txt = txt.replace('\\\\u2019', '\u2019')
    # txt = txt.replace('\\u2019', '\u2019')


    data=txt.split('\n<|endoftext|>\n')
    print('0')
    print(data[0])
    print('100')
    print(data[100])
    print('over')

data=list(map(lambda x:{'text':x},data))


with open(path.replace('txt','json'), 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)
