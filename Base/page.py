"""统一入口类,返回页面类,实例化对象"""
from Page.searchPage import SearchPage
from Page.settingPage import SettingPage
from Page.showPage import ShowPage


class Page:

    @classmethod
    def get_settingPage(cls):
        """返回设置页面实例化对象"""
        return SettingPage()

    @classmethod
    def get_showPage(cls):
        """返回显示页面的实例化对象"""
        return ShowPage()

    @classmethod
    def get_searchPage(cls):
        return SearchPage()