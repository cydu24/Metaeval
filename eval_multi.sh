# 切换到指定的目录
cd /data1/dcy/projects/evaluate/openchat-master/evaluation

# 激活Conda环境
source activate dcy_infer2
export CUDA_VISIBLE_DEVICES=3,4
python /data1/dcy/projects/evaluate/openchat-master/evaluation/run_eval_multi.py \
    --model /data1/dcy/projects/fine-tune/fine-tune-yyz/train/output/5-3_12:35_vicuna-13b/ckpt/vicuna-13b_10000 \
    --model_type vicuna \
    --data_path /data1/dcy/projects/evaluate/openchat-master/evaluation/eval_data_dcy \
    --eval_sets "fs_cothub/mmlu" "zs/math" "zs/mgsm" "coding/humaneval"  "zs/truthfulqa_orca" "zs/agieval" "zs/bbh_mc_orca" "zs/drop"\
    --output_path /data1/dcy/projects/evaluate/openchat-master/evaluation/res \
    --rounds 4 \
    --max_token 4096 \
    --output_dir output \
    --save_name vicuna-13b

# # 切换到指定的目录
# cd /data1/dcy/projects/evaluate/openchat-master/evaluation

# # 激活Conda环境
# source activate dcy_infer2
# export CUDA_VISIBLE_DEVICES=5,7
# python /data1/dcy/projects/evaluate/openchat-master/evaluation/run_eval_multi.py \
#     --model /data1/dcy/projects/fine-tune/fine-tune-yyz/train/output/5-1_00:12_Meta-Llama-3-8B-Instruct/ckpt/Meta-Llama-3-8B-Instruct_10000 \
#     --model_type llama3 \
#     --data_path /data1/dcy/projects/evaluate/openchat-master/evaluation/eval_data_dcy \
#     --eval_sets "fs_cothub/mmlu" "fs_cothub/svamp" "fs_cothub/gsm8k" "zs/math" "zs/mgsm" "coding/humaneval"  "zs/truthfulqa_orca" "zs/agieval" "zs/bbh_mc_orca" "zs/drop"\
#     --output_path /data1/dcy/projects/evaluate/openchat-master/evaluation/res \
#     --rounds 4 \
#     --max_token 4096 \
#     --output_dir output \
#     --save_name llama3-8b





