"""设置页面操作"""
from Base.base import Base
from Page.pageElements import PageElements


class SettingPage(Base):

    # 初始化Base类init
    def __init__(self):
        super().__init__()

    def click_search_btn(self):
        """点击搜索按钮方法"""
        self.click_ele(PageElements.search_btn_id)

    def click_show_btn(self):
        """点击按钮"""
        self.click_ele(PageElements.setting_show_btn_xpath)