import torch
import json
from vllm import LLM, SamplingParams
from transformers import AutoModelForCausalLM, AutoTokenizer
from human_eval.data import read_problems


infer_template = "[INPUT] Please implement the python function. Only output the function, without any explainations. from typing import List\n\n\def get_sum(a: List[int]) -> int:\n  \"\"\"calculate the sum of an integer array.\"\"\" [/INPUT] [OUTPUT] '''python\ndef get_sum(a: List[int]):\n  sum = 0\n   for x in a:\n       sum += x\n  return sum\n''' [/OUTPUT] [INPUT] {task} [/INPUT] [OUTPUT] "
def get_instr(prompt):
    return infer_template.format(task=prompt)
import ray

def initialize_model(model_path):
    
    
    model = LLM(
        model=model_path, 
        trust_remote_code=True,
        tensor_parallel_size=torch.cuda.device_count(),
    )
    return model


def vllm_generate(vllm_model, prompts, use_tqdm=True):
    """传入文本prompts, 返回推理结果, 输入过长的返回<input length exceeded>"""
    sampling_params = SamplingParams(
        max_tokens=512,
        stop=['</s>', '[/OUTPUT]'],
    )
    generated_texts = []
    prompts_list = []
    prompts_per_step = 10000  # 最多批量推理多少prompts
    for i in range(0, len(prompts), prompts_per_step):
        prompts_list.append(prompts[i:i+prompts_per_step])

    for i, inputs in enumerate(prompts_list):
        outputs = vllm_model.generate(inputs, sampling_params, use_tqdm=use_tqdm)
        for i in range(len(outputs)):
            output = outputs[i]
            generated_text = output.outputs[0].text
            generated_texts.append(generated_text)
    return generated_texts


def get_sample_file(model_path, output_file, cnt=164):
    problems = read_problems()
    prompts = []
    for i in range(cnt):
        prompt = get_instr(problems[f"HumanEval/{i}"]["prompt"])
        prompts.append(prompt)
    
    vllm_model = initialize_model(model_path)
    generated_texts = vllm_generate(vllm_model, prompts)
    with open(output_file, "w") as f, open("2.txt", "w") as f2:
        for i in range(len(generated_texts)):
            text = generated_texts[i].strip()
            function_prefix = "def " + problems[f"HumanEval/{i}"]["entry_point"]
            try:
                completion = function_prefix + text.split(function_prefix)[1]
                if completion.endswith("```"):
                    completion = completion[:-3]
            except:
                completion = "format error"
            print(json.dumps({
                "task_id": f"HumanEval/{i}",
                "origin_output": generated_texts[i],
                "completion": completion
            }), file=f)

            print(problems[f"HumanEval/{i}"]["prompt"], file=f2)
            print(generated_texts[i] + "\n", file=f2)


if __name__ == "__main__":
    model_path = "/data1/yyz/downloads/models/MetaMath-Llemma-7B"
    model_path = "/data1/dcy/downloads/model/meta-llama/Meta-Llama-3-70B-Instruct"
    model_path = "/data1/dcy/downloads/model/google/gemma-2b-it"
    get_sample_file(model_path, "output.jsonl") 
    