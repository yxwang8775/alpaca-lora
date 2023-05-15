N=5



CUDA_VISIBLE_DEVICES=${N} python finetune.py \
    --base_model '/nvme/wangyaoxiang/model/llama-7b-hf/snapshots/5f98eefcc80e437ef68d457ad7bf167c2c6a1348' \
    --data_path 'yahma/alpaca-cleaned' \
    --output_dir '/nvme/wangyaoxiang/model/lora-alpaca2'
