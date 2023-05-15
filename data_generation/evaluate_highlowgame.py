from highlowgame import HighLowGame
from model_wrapper import ModelWrapper
print(0)
model=ModelWrapper(model_name='decapoda-research/llama-7b-hf',checkpoint='/nvme/wangyaoxiang/model/llama-7b-hf/snapshots/5f98eefcc80e437ef68d457ad7bf167c2c6a1348')
print(1)
task=HighLowGame(high=1000000)
print(2)
print(task.evaluate_model(model=model))