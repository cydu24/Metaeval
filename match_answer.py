# bbh codeeval zs/math 得改 bbh没用跟随指令 codeeval报错 zs/math好像是latex 不好抽取标准答案 
#gsm8k还没写好
# mgsm math很难 不太行 mgsm有.0 得标准化自己写一个
import argparse
from glob import glob
import json
import os
import json
from scipy.optimize import linear_sum_assignment
from tqdm import tqdm
from eval_task.drop_dataset import zs_drop_match_answer
from eval_task.humaneval import coding_humaneval_match_answer
from eval_task.bbh import fs_cothub_bbh_match_answer
from eval_task.gsm8k import fs_cothub_gsm8k_match_answer
from eval_task.agieval import zs_agieval_match_answer
from eval_task.mmlu import fs_cothub_mmlu_match_answer
from eval_task.svamp import fs_cothub_svamp_match_answer
from eval_task.mgsm import zs_mgsm_match_answer
from eval_task.math_dataset import fs_cothub_math_match_answer
from eval_task.truthfulqa import fs_cothub_truthfulqa_match_answer

MATCH_ANSWER_FUNCTION = {
    # multi task 
    "fs_cothub/mmlu": fs_cothub_mmlu_match_answer,
    # prompt要改 没有要求 也是选择题
    "zs/agieval": zs_agieval_match_answer,
    # 综合能力
    "fs_cothub/bbh": fs_cothub_bbh_match_answer,
    "zs/bbh_mc_orca": fs_cothub_bbh_match_answer,
    # math
    "fs_cothub/svamp": fs_cothub_svamp_match_answer,
    "fs_cothub/gsm8k": fs_cothub_gsm8k_match_answer,
    "zs/math": fs_cothub_math_match_answer,
    # mgsm
    "zs/mgsm": zs_mgsm_match_answer,
    # code
    "coding/humaneval": coding_humaneval_match_answer,
    # 价值对齐
    "zs/truthfulqa_orca": fs_cothub_truthfulqa_match_answer,
    # 推理能力 阅读理解
    "zs/drop": zs_drop_match_answer,
}


def view_results(model_path, rounds):
    eval_results = []
    print ("starting")
    for filename in glob(os.path.join(model_path, "inference_result", "*.json"), recursive=True):  
        task_name = os.path.splitext(filename[len(model_path):])[0].strip("/")
        task_name = os.path.basename(task_name)
        task_name = task_name[:-2].replace("_", "/")  # 删除最后的 "_4"将下划线"_" 替换为斜杠 "/"
        print(task_name)
        # task_name == "coding/humaneval" or
        if  task_name == "zs/math" or task_name == "zs/bbh/mc/orca" :
            continue
        if task_name != "zs/mgsm":
            continue
        output_data = []
        with open(filename, "r") as f:
            questions = json.loads(f.read())
            result_task = [{
            "model_name":model_path,
            "filename":filename,
            "task_name":task_name,
            "lens":len(questions),
            "t2f_2":0,
            "t2f_3":0,
            "t2f_4":0,   
            "f2t_2":0,
            "f2t_3":0,
            "f2t_4":0,
            "cnt_1":0,
            "cnt_2":0,    
            "cnt_3":0,
            "cnt_4":0,
            "percent_1":0,
            "percent_2":0,
            "percent_3":0,
            "percent_4":0,
            }] 
            
            for q in tqdm(questions):
                output_data.append({
                "question": q['question'],
                "model_generate1": "",
                "model_generate2": "",
                "model_generate3": "",
                "model_generate4": "",
                "judge1":0,
                "judge2":0,
                "judge3":0,
                "judge4":0,
                "origi_result": "",
                "model_result1": "",
                "model_result2": "",
                "model_result3": "",
                "model_result4": "",
                })
                
                task_type = q.get('task_type')
                for round_idx in range(1, rounds + 1): 
                    q[f"judge{round_idx}"], output_data[-1][f"origi_result"], q[f"model_result{round_idx}"] = MATCH_ANSWER_FUNCTION[q['task_type']](q, q[f"output{round_idx}"])
                    # print(f"output = {q[f'output{round_idx}']}")
                    output_data[-1][f"model_generate{round_idx}"] = q[f'output{round_idx}']
                    output_data[-1][f"model_result{round_idx}"] = q[f"model_result{round_idx}"]
                    output_data[-1][f"judge{round_idx}"] = q[f"judge{round_idx}"]
  
                    if output_data[-1][f"judge{round_idx}"] == True:
                        result_task[-1][f"cnt_{round_idx}"] = result_task[-1][f"cnt_{round_idx}"] + 1
                    
                    if round_idx > 1 and output_data[-1][f"judge{round_idx}"] == True and output_data[-1][f"judge{round_idx-1}"] == False:
                        result_task[-1][f"f2t_{round_idx}"] = result_task[-1][f"f2t_{round_idx}"] + 1
                    if round_idx > 1 and output_data[-1][f"judge{round_idx-1}"] == True and output_data[-1][f"judge{round_idx}"] == False:
                        result_task[-1][f"t2f_{round_idx}"] = result_task[-1][f"t2f_{round_idx}"] + 1
                for round_idx in range(1, rounds + 1): 
                    result_task[-1][f"percent_{round_idx}"] = result_task[-1][f"cnt_{round_idx}"] /(result_task[-1]["lens"]/3)
        save_task_name = os.path.splitext(filename[len(model_path):])[0].strip("/")
        save_task_name = os.path.basename(save_task_name)
        save_path = os.path.join(model_path, "view_result", save_task_name)     
        os.makedirs(save_path, exist_ok=True)
        with open (f"{save_path}/output.json", "w") as f:
            json.dump(output_data, f, indent=2)
        with open (f"{save_path}/summary.json", "w") as f:
            json.dump(result_task, f, indent=2)    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", type=str, default="/data1/dcy/projects/evaluate/evaluation_all/output/5-6_00:39_llama3-8b_4rounds")
    parser.add_argument("--rounds", type=int, default=4)
    args = parser.parse_args()
    view_results(**vars(args))
if __name__ == "__main__":
    main()