import os

import allure
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

    @allure.severity(allure.severity_level.BLOCKER)     # 最重要的用
    @allure.step("测试步骤a+b = c")
    @pytest.mark.parametrize("a, b, c", sum_data())
    def test_sum_001(self, a, b, c):

        # 添加描述信息
        allure.attach("我是步骤描述", "附件名字")
        print("\n{}+{}={}".format(a,b,c))
        assert a+b == c

    @allure.severity(allure.severity_level.CRITICAL)     # 比较重要的用例
    def test_sum_002(self):
        assert True

    @allure.severity(allure.severity_level.NORMAL)     # 正常的用例
    def test_sum_003(self):
        assert True

    @allure.severity(allure.severity_level.MINOR)     # 比一般低一些的用例
    def test_sum_004(self):
        assert True

    @allure.severity(allure.severity_level.TRIVIAL)     # 可以忽略的用例
    def test_sum_005(self):
        assert True