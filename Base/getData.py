import os
import yaml


class GetData:
    """读取各种类型的数据"""

    @classmethod
    def get_yaml_data(self, name):
        """
        读取yaml数据
        :param name: 文件名称
        :return: yaml数据
        """
        # data目录是固定的
        with open("./data" + os.sep + name, "r", encoding="utf-8") as f:
            # 读文件
            return yaml.safe_load(f)

