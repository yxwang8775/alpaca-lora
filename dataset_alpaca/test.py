from datasets import load_dataset
from template import PATTERNS
dataset = load_dataset('aeslc',split='validation')
print(len(dataset))
print(dataset.__getitem__(0))
print(dataset.format['columns'])
