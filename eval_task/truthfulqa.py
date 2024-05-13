

from .drop_dataset import _normalize_answer
import re
def clean_numbers(numbers):
    # 清理每个元素，去掉所有非数字字符，并且特别处理末尾的句号
    cleaned = [_normalize_answer(num) for num in numbers]
    return cleaned
def fs_cothub_truthfulqa_match_answer(q, response):


    pattern1 = '([A-Da-d])'
    patterns2 = [
    '\s*The answer is \s*\(([A-Da-d])\)\s*',
    '\s*The answer is \s*([A-Da-d])\)\s*',
    '\s*The answer is \s*([A-Da-d])\s*',
    '\s*So, the final answer is \(([A-Da-d])\)',
    '\s*So, the final answer is ([A-Da-d])\)',
    '\s*So, the final answer is ([A-Da-d])',
    '\s*The answer is: \(([A-Da-d])\)',
    '\s*The answer is: ([A-Da-d])\)',
    '\s*The answer is: ([A-Da-d])',
    '\s*The correct answer is \(([A-Da-d])\)',
    '\s*The correct answer is ([A-Da-d])\)',
    '\s*The correct answer is ([A-Da-d])',
    '\s*The answer is: \(([A-Da-d])\)',
    '\s*The answer is: ([A-Da-d])\)',
    '\s*The answer is: ([A-Da-d])',

    '\s*The correct answer is \(([A-Da-d])\)',
    '\s*The correct answer is ([A-Da-d])\)',
    '\s*The correct answer is ([A-Da-d])',
    '\s*The answer is \(([A-Da-d])\):',
    '\s*The answer is \(([A-Da-d])\).',
    '\s*\(?([A-Da-d])\)?:',
    '\s*\(?([A-Da-d])\)?\.',
    '\s*the correct answer would be \s*([A-Da-d])\s*'
    ]
    # Extract numbers from the answer and response
    ans_numbers = re.findall(pattern1, q["label"][-1])
    
    # 尝试每个模式直到找到匹配项
    pred_numbers = []
    for pa in patterns2:
        pred_numbers = re.findall(pa, response)
        if pred_numbers:
            break  # 找到匹配后立即退出循环
    if ans_numbers and pred_numbers:
        # Compare the last number found in both answer and response
        if ans_numbers[-1] == pred_numbers[-1]:
            return True, ans_numbers[-1], pred_numbers[-1]  # Match found, return 1 and the matching number
        else:
            return False, ans_numbers[-1], pred_numbers[-1]  # Numbers do not match, return 0 and the last number from the response

    return False, ans_numbers[-1], "No match or missing numbers"  # No numbers found or other issues


