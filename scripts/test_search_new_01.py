import pytest, time

from Base.getData import GetData
from Base.page import Page
from Base.driver import Driver


def search_data():
    # 定义空列表
    search_list = []
    data = GetData.get_yaml_data("data_search.yml")
    for i in data.values():
        #添加元祖数据到列表
        search_list.append((i.get("search_data"), i.get("exp_data")))
    return search_list


class TestSearch:

    # def setup_class(self):
    #     # 实例化页面类
    #     Page.get_searchPage()

    def teardown_class(self):
        """退出driver"""
        Driver.quit_app_driver()

    # 因为只需要运行一次 并且是依赖方法，所以使用fixture工厂函数
    @pytest.fixture(scope="class", autouse=True)
    def click_search_btn(self):
        """点击搜索按钮 并且 点击一次"""
        Page.get_settingPage().click_search_btn()

    @pytest.mark.parametrize("search_data, exp_data", search_data())
    def test_search_text(self, search_data, exp_data):
        """
        搜索测试方法
        :param search_data: 输入内容
        :param exp_data: 预期结果
        :return:
        """
        # 输入框输入内容
        Page.get_searchPage().search_text(search_data)
        # 断言
        assert exp_data in Page.get_searchPage().get_search_result()
