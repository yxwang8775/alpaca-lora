
python finetune.py \
    --base_model '/mnt/petrelfs/share_data/nlp_llama_hf/models--decapoda-research--llama-7b-hf/snapshots/5f98eefcc80e437ef68d457ad7bf167c2c6a1348' \
    --data_path 'yahma/alpaca-cleaned' \
    --output_dir './lora-alpaca-test' \
    --batch_size 128 \
    --micro_batch_size 4 \
    --num_epochs 3

