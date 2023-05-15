N=4


CUDA_VISIBLE_DEVICES=${N} python finetune.py \
    --base_model '/nvme/wangyaoxiang/model/llama-7b-hf/snapshots/5f98eefcc80e437ef68d457ad7bf167c2c6a1348' \
    --data_path './dataset_alpaca/dataset_alpaca_gen.json' \
    --output_dir '/nvme/wangyaoxiang/model/lora-alpaca_gen' \
    --batch_size 128 \
    --micro_batch_size 64
