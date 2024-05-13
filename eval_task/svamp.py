from .drop_dataset import _normalize_answer
import re
def clean_numbers(numbers):
    # 清理每个元素，去掉所有非数字字符，并且特别处理末尾的句号
    cleaned = [_normalize_answer(num) for num in numbers]
    return cleaned
def fs_cothub_svamp_match_answer(q, response):
    pattern1 = '####.*?(\d*\.?\d+)'
    patterns2 = [
    'So, the final answer is \$\s*(\d+\.?\d*)\s*',
    'The answer is: \s*(\d+\.?\d*)',
    'Therefore, the final answer is \$\s*(\d+\.?\d*)',
    'Therefore, the final answer is \s*(\d+\.?\d*)',
    'So, the final answer is \s*(\d+\.?\d*)'
]
    # Extract numbers from the answer and response
    ans_numbers = q["answer"]
    # 尝试每个模式直到找到匹配项
    pred_numbers = []
    for pa in patterns2:
        pred_numbers = re.findall(pa, response)
        if pred_numbers:
            break  # 找到匹配后立即退出循环
    # Extract numbers from the answer and response
        pred_numbers = re.findall(pa, response)
    pred_numbers = clean_numbers(pred_numbers)
    # Check if both answer and response contain numbers and compare the last found number
    if ans_numbers and pred_numbers:
        # Compare the last number found in both answer and response
        
        if ans_numbers == pred_numbers[-1]:
            return True, ans_numbers, pred_numbers[-1]  # Match found, return 1 and the matching number
        else:
            return False, ans_numbers, pred_numbers[-1]  # Numbers do not match, return 0 and the last number from the response

    return False, ans_numbers, "No match or missing numbers"  # No numbers found or other issues