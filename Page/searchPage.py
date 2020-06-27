from selenium.webdriver.common.by import By
from Base.base import Base
from Page.pageElements import PageElements


class SearchPage(Base):

    def __init__(self,):
        # 实例化Base类
        # self.base_obj = Base()
        # 使用继承
        super().__init__()
        # 页面元素
        # 搜索按钮
        # self.search_btn_id = (By.ID, "com.android.settings:id/search")
        # # 搜索输入框
        # self.search_input_id = (By.ID, "android:id/search_src_text")
        # # 搜索结果
        # self.search_result_ids = (By.ID, "com.android.settings:id/title")

    # def click_search_btn(self):
    #     """点击搜索按钮方法"""
    #     self.click_ele(PageElements.search_btn_id)

    def search_text(self, text):
        """
        搜索内容方法
        :param text: 搜索输入文本内容
        :return:
        """
        self.send_ele(PageElements.search_input_id, text)

    def get_search_result(self):
        """获取搜索结果方法"""
        # 定位搜索结果
        results = self.search_eles(PageElements.search_result_ids)
        return [i.text for i in results]
