import datetime
import json
import argparse
import os
import asyncio
from glob import glob
from collections import defaultdict
import orjson
import torch
from tqdm import tqdm
from vllm import LLM, SamplingParams
from match_answer import MATCH_ANSWER_FUNCTION
# import logging
# logging.basicConfig(level=logging.WARNING)
import os
'''
os.environ["CUDA_VISIBLE_DEVICES"] = "5,7"
export CUDA_VISIBLE_DEVICES=1
'''
from prompt_format import MMLU_ANSWER_PATTERN,MMLU_INSTRUCTION,MATH_INSTRUCTION,truthfulqa_INSTRUCTION,agieval_INSTRUCTION,bbh_INSTRUCTION,grop_INSTRUCTION,humaneval_INSTRUCTION
from model_format import format_llama3_answer, format_vicuna_answer, format_test_answer, format_llama2_answer
def format_dialogue(query, history, model_type, task_type):
    tast_prompt = ""
    if task_type == "fs_cothub/mmlu":
        tast_prompt = MMLU_INSTRUCTION
    elif task_type == "fs_cothub/svamp":
        tast_prompt = MATH_INSTRUCTION
    elif task_type == "fs_cothub/gsm8k":
        tast_prompt = MATH_INSTRUCTION
    elif task_type == "zs/math":
        tast_prompt = MATH_INSTRUCTION
    elif task_type == "zs/mgsm":
        tast_prompt = MATH_INSTRUCTION
    elif task_type == "coding/humaneval":
        tast_prompt = humaneval_INSTRUCTION
    elif task_type == "zs/truthfulqa_orca":
        tast_prompt = truthfulqa_INSTRUCTION
    elif task_type == "zs/agieval":
        tast_prompt = agieval_INSTRUCTION    
    elif task_type == "zs/bbh_mc_orca":
        tast_prompt = bbh_INSTRUCTION 
    elif task_type == "zs/drop":
        tast_prompt = grop_INSTRUCTION
    else:
        tast_prompt = ""
    prompt = ""
    if model_type == "llama2":
        prompt = format_llama2_answer(tast_prompt = tast_prompt, query = query, history= history)
    elif model_type == "vicuna":
        # prompt = format_test_answer(tast_prompt=tast_prompt,query = query, history=history)
        prompt = format_vicuna_answer(tast_prompt=tast_prompt,query = query, history=history)
    elif model_type == "llama3":
        prompt = format_llama3_answer(tast_prompt=tast_prompt,query = query, history=history)
    else:
        prompt = format_test_answer(tast_prompt=tast_prompt,query = query, history=history)
    return prompt
def prompts_func(questions, model_type, task_type):
        # Construct conversation
    prompt_indices = []
    conversations = []
    for idx, q in enumerate(questions):
        q = format_dialogue(q["question"], (), model_type, task_type)
        conversations.append(q)
        prompt_indices.append(idx)
    return conversations, prompt_indices
def get_model_answers_with_follow_up(model,questions,model_type,rounds ,engine,sampling_params,task_type):
    refine_query = "Please further think about and give me a more precise and professional Answer: " 
    # refine_query = "Give me a better A:"
    prompts, prompt_indices = prompts_func(questions, model_type, task_type)
    for round_idx in range(1, rounds + 1):  # 循环执行指定轮次的推理
        responses = engine.generate(prompts, sampling_params=sampling_params)
        next_prompts = []  # 准备下一轮的prompts
        for idx, resp in zip(prompt_indices, responses):
            ans = resp.outputs[0].text
            questions[idx][f"input{round_idx}"] = prompts[idx]
            questions[idx][f"output{round_idx}"] = ans
            if round_idx == 1:
                questions[idx][f"question{round_idx}"] = questions[idx]["question"]
            else:
                questions[idx][f"question{round_idx}"] = refine_query

            if round_idx == rounds:
                questions[idx][f"response"] = ans
            if round_idx < rounds:  # 如果不是最后一轮，准备下一轮的输入
                # 更新历史记录来准备下一轮的prompts
                # history = [(questions[idx][f"question{i}"], questions[idx][f"output{i}"]) for i in range(1, round_idx + 1)]
                history = [(questions[idx][f"question{1}"], questions[idx][f"output{round_idx}"])]
                last_input = questions[idx][f"question{round_idx}"]
                last_output = questions[idx][f"output{round_idx}"]
                next_prompts.append(format_dialogue(refine_query, history, model_type, task_type))
        prompts = next_prompts 
    return questions
def run_eval(model,  model_type,data_path,eval_sets,output_path,  rounds ,  max_token,output_dir,save_name):
    os.makedirs(output_path, exist_ok=True)
    t = datetime.datetime.now()
    config = {
        "model":model,
        "model_type": model_type,
        "data_path": data_path,
        "eval_sets": eval_sets,
        "output_path": output_path,
        "rounds": rounds,
        "max_token": max_token,
        "output_dir": output_dir,
        "save_name": save_name,
    }
    save_dir = f"{output_dir}/{t.month}-{t.day}_{t.hour:02d}:{t.minute:02d}_{save_name}_{rounds}rounds"
    os.makedirs(save_dir, exist_ok=True)
    with open(f"{save_dir}/config.json", "w") as f:
        print(json.dumps(config, indent=4), file=f)
    tasks_data = defaultdict(list)
    for filename in glob(os.path.join(data_path, "**", "*.jsonl"), recursive=True):
        task_name = os.path.splitext(filename[len(data_path):])[0].strip("\\/")
        print(task_name)
        task_type = os.path.dirname(task_name)
        assert task_type in MATCH_ANSWER_FUNCTION
        if eval_sets and not sum([task_name.startswith(a) for a in eval_sets]):
            continue
        print(filename)
        with open(filename, "r") as f:
            task_data = list(map(orjson.loads, f.readlines()))
        tasks_data[task_type].extend([{**item, "task_name": task_name, "task_type": task_type, "response": ""} for item in task_data])
    engine = LLM(model,
                 max_num_batched_tokens=4096,
                 max_model_len=4096,
                 tensor_parallel_size=torch.cuda.device_count(),
                 )
    sampling_params = SamplingParams(
        temperature=0.7,  # 降低随机性，增加确定性
        top_p=0.9,  # 考虑较高概率的词汇，但不是所有的
        frequency_penalty =0.5,  # 适度惩罚重复的词汇
        presence_penalty=0.5,  # 适度惩罚已经出现的词汇
        repetition_penalty=1.2,  # 适度鼓励新词汇的使用
        max_tokens=max_token,  # 根据需要生成的内容长度来调整
        stop=['</s>',])
    for task_type, questions in tqdm(tasks_data.items(), desc="处理任务"):
        print(f"正在处理任务类型：{task_type}，共有{len(questions)}个问题。")
        questions = get_model_answers_with_follow_up(model, questions, model_type, rounds,engine,sampling_params, task_type)
        inference_result = os.path.join(save_dir, "inference_result")
        os.makedirs  (inference_result, exist_ok=True) 
        safe_task_type = task_type.replace("/", "_")
        with open(os.path.join(inference_result, f'{safe_task_type}_{rounds}.json'), 'w') as f: 
            json.dump(questions, f, indent=2)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default="/data1/dcy/projects/fine-tune/fine-tune-yyz/train/output/5-3_12:35_vicuna-13b/ckpt/vicuna-13b_10000")
    parser.add_argument("--model_type", type=str, default="vicuna")
    parser.add_argument("--data_path", type=str, default="/data1/dcy/projects/evaluate/openchat-master/evaluation/eval_data_test")
    parser.add_argument("--eval_sets", type=str, nargs="+", default=["fs_cothub/mmlu","fs_cothub/svamp","fs_cothub/gsm8k","zs/math","zs/mgsm","coding/humaneval", "zs/truthfulqa_orca","zs/agieval","zs/bbh_mc_orca","zs/drop",])
    # parser.add_argument("--eval_sets", type=str, nargs="+", default=["zs/math","zs/mgsm","zs/agieval","zs/bbh_mc_orca","zs/drop",])
    parser.add_argument("--output_path",   type=str, default="/data1/dcy/projects/evaluate/openchat-master/evaluation/res")
    parser.add_argument("--rounds", type=int, default=3)
    parser.add_argument("--max_token", type=int, default=2048)
    parser.add_argument("--output_dir", type=str, default="output", help="the dir to save outputs")
    parser.add_argument("--save_name", type=str, default="vicuna-13b", help="save model in: ./output_dir/save_name+time/ckpt_dir/save_name")
    args = parser.parse_args()
    run_eval(**vars(args), )
if __name__ == "__main__":
    main()
    