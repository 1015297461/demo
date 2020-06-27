import os
import pytest
import yaml
from Base.getData import GetData
from data.read_sum_yml import read_yml


def sum_data():

    # 定义空列表
    sum_list = []

    data = GetData.get_yaml_data("data_sum.yml")
    for i in data.values():
        #添加元祖数据到列表
        sum_list.append((i.get("a"), i.get("b"), i.get("c")))
    return sum_list


class TestSum:

    @pytest.mark.parametrize("a, b, c", sum_data())
    def test_sum(self, a, b, c):

        print("\n{}+{}={}".format(a,b,c))
        assert a+b == c