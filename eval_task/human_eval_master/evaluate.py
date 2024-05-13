from human_eval.evaluation import evaluate_functional_correctness
from get_sample_file import get_sample_file

def evaluate_model_humaneval(model_path, output_file, limit=164):
    # get_sample_file(model_path, output_file, limit)
    return evaluate_functional_correctness(output_file)
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["CUDA_VISIBLE_DEVICES"] = "1,2,3,4"
if __name__ == "__main__":
    # model_path = "/data1/dcy/downloads/model/lmsys/vicuna-33b-v1.3"
    # model_path = "/data1/yyz/downloads/models/CodeLlama-7b-hf"
    model_path = "/data1/dcy/downloads/model/meta-llama/Meta-Llama-3-70B-Instruct"
    # model_path = "/data1/dcy/downloads/model/Qwen/Qwen-72B-Chat"
    result = evaluate_model_humaneval(model_path, f"{model_path.split('/')[-1]}_output.jsonl")
    print(result) 