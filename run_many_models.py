import os
import subprocess
import time

def get_available_gpus(min_free_memory=80000, min_available_gpus=1):
    """
    获取系统中满足最小空闲内存要求的可用GPU编号列表。
    :param min_free_memory: 每张GPU至少需要的空闲内存（以MB为单位）。
    :param min_available_gpus: 至少需要的可用GPU数量。
    :return: 可用的GPU编号列表。如果可用GPU数量小于min_available_gpus，返回空列表。
    """
    # 使用nvidia-smi查询GPU使用情况
    result = subprocess.run(['nvidia-smi', '--query-gpu=index,memory.free', '--format=csv,noheader,nounits'], capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError("无法查询GPU状态")

    # 分析每个GPU的编号和可用内存
    available_gpus = []
    for line in result.stdout.strip().split('\n'):
        gpu_id, free_memory = line.split(', ')
        if int(free_memory) >= min_free_memory:
            available_gpus.append(gpu_id)

    if len(available_gpus) >= min_available_gpus:
        return available_gpus[:min_available_gpus]  # 返回满足条件的前N张卡的编号
    else:
        return []

def wait_for_gpus(interval=1, min_free_memory=77824, min_available_gpus=1, patience=1):
    """
    等待直到系统中至少有指定数量的GPU变得可用，并在它们连续空闲一定时间后返回这些GPU的编号。
    :param interval: 检查间隔时间（秒）。
    :param min_free_memory: 每张GPU至少需要的空闲内存（以MB为单位）。
    :param min_available_gpus: 至少需要的可用GPU数量。
    :param patience: 必须连续空闲的时间（秒）。
    :return: 可用的GPU编号列表。
    """
    print("等待至少{}张GPU资源可用...".format(min_available_gpus))
    start_time = {}  # 记录开始空闲的时间
    while True:
        available_gpus = get_available_gpus(min_free_memory, min_available_gpus)
        current_time = time.time()
        for gpu in available_gpus:
            if gpu not in start_time:
                start_time[gpu] = current_time  # 开始记录空闲时间
            elif current_time - start_time[gpu] >= patience:
                print("编号为{}的GPU已连续空闲超过{}秒。".format(gpu, patience))
            else:
                # 如果当前GPU不再空闲，重置开始时间
                if gpu in start_time:
                    del start_time[gpu]

        # 检查是否有足够数量的GPU已经空闲了足够长的时间
        ready_gpus = [gpu for gpu, t in start_time.items() if current_time - t >= patience]
        if len(ready_gpus) >= min_available_gpus:
            print("现在至少有{}张GPU可用，编号为：{}".format(min_available_gpus, ', '.join(ready_gpus)))
            return ready_gpus[:min_available_gpus]  # 返回满足条件的前N张卡的编号
        else:
            time.sleep(interval)


args_list = [    
    # {
    #     "rounds":1,
    #     "output_file": "/data1/dcy/projects/openchat-master/ochat/evaluation/eval_results/my_llama2_moe_ans3_rounds1.json"
    # },
    # {
    #     "rounds":2 ,
    #     "output_file": "/data1/dcy/projects/openchat-master/ochat/evaluation/eval_results/my_llama2_moe_ans3_rounds2.json"
    # },
    # {
    #     "rounds":3 ,
    #     "output_file": "/data1/dcy/projects/openchat-master/ochat/evaluation/eval_results/my_llama2_moe_ans3_rounds3.json"
    # },
    {
        "rounds":4,
        "output_file": "/data1/dcy/projects/openchat-master/ochat/evaluation/eval_results/my_llama2_moe_ans3_rounds4.json"
    },
]

if __name__ == "__main__":

    
    instruction_template = "CUDA_VISIBLE_DEVICES={cuda_visible_devices} python /data1/dcy/projects/openchat-master/ochat/evaluation/run_eval_ans3.py --rounds {rounds} --output_file {output_file}"
    
    for args in args_list:
        available_gpus = wait_for_gpus()  # 等待至少有两张GPU变得可用
        cuda_visible_devices = ','.join(available_gpus)  # 将可用的GPU编号转换为字符串

        # 使用可用的GPU编号来设置CUDA_VISIBLE_DEVICES环境变量
        os.environ['CUDA_VISIBLE_DEVICES'] = cuda_visible_devices
        instr = instruction_template.format(
            cuda_visible_devices=cuda_visible_devices,  # 引用CUDA设备
            rounds=args["rounds"],
            output_file=args["output_file"],
        )
        try:
         os.system(instr)
        except Exception as e:
            print(e)
            break

