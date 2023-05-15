
export CUDA_VISIBLE_DEVICES=4

python finetune.py \
    --base_model '/nvme/wangyaoxiang/model/llama-7b-hf/snapshots/5f98eefcc80e437ef68d457ad7bf167c2c6a1348' \
    --data_path 'yahma/alpaca-cleaned' \
    --output_dir '/nvme/wangyaoxiang/model/lora-alpaca-seize' \
    --batch_size 128 \
    --micro_batch_size 4 \
    --num_epochs 100

