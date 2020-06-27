import os
import yaml


def read_yml():
# 定义空列表
    sum_list = []

    # 打开文件
    with open("./data" + os.sep + "data_sum.yml", "r", encoding="utf-8") as f:
        # 读文件
        data = yaml.safe_load(f)
        print("data", data)
        # print("value", data.values())
        for i in data.values():
            # print("i:", (i.get("a"), i.get("b"), i.get("c")))
            sum_list.append((i.get("a"), i.get("b"), i.get("c")))
        # print(sum_list)
    return sum_list