from collections import defaultdict, Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Union, Iterable, Dict

from .human_eval_master.human_eval.data import HUMAN_EVAL, read_problems, stream_jsonl, write_jsonl
from .human_eval_master.human_eval.execution import check_correctness
# from human_eval_master.human_eval.data import HUMAN_EVAL, read_problems, stream_jsonl, write_jsonl
# from human_eval_master.human_eval.execution import check_correctness


def coding_humaneval_match_answer(task_data, response):
    task_id = task_data["task_id"]
    completion = response
    results = defaultdict(list)
    completion_id = task_id.split("/")[-1]
    print(f"counter = {task_id}")
    problems = read_problems(HUMAN_EVAL)
    print(problems[task_id])
    print(completion)
    text = completion.strip()
    function_prefix = "def " + problems[task_id]["entry_point"]
    # match = [
    #     "'''",
    #     "```",
    #     "\'\'\'"
    # ]
    try:
        function_text = text[text.rfind("```python\n"):text.rfind("\n```")]
        completion = function_prefix + function_text.split(function_prefix)[1]
    except:
        completion = "format error"
    print(f"completion after = \n{completion}")
    future = check_correctness(problem=problems[task_id], completion=completion, timeout=3.0,
                      completion_id= completion_id)
    print(future)
    if future['passed'] == True:
        return True, future['completion_id']  , future['passed']         
    else:
        return False, future['completion_id']  , future['passed']
            
if __name__ == "__main__":
    task_data ={"task_id": "HumanEval/49", "origin_output": " ```python\ndef modp(n: int, p: int):\n    \"\"\"Return 2^n modulo p (be aware of numerics).\"\"\"\n    return pow(2, n) % p\n```", "completion": "def modp(n: int, p: int):\n    \"\"\"Return 2^n modulo p (be aware of numerics).\"\"\"\n    return pow(2, n) % p", "result": "passed", "passed": True}
    ans = coding_humaneval_match_answer(task_data, task_data["origin_output"])
    print(ans)