"""设置字体自动化脚本"""
from Base.driver import Driver
from Base.page import Page


class TestSetFont:

    def teardown_class(self):
        # 退出driver
        Driver.quit_app_driver()

    def test_set_font(self):
        # 设置页面-点击显示
        Page.get_settingPage().click_show_btn()
        # 显示页面-选择字体
        Page.get_showPage().click_font()
        # 显示页面-获取信息-断言
        assert "普通" in Page.get_showPage().get_summary_list()