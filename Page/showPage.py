"""显示界面"""
from Base.base import Base
from Page.pageElements import PageElements


class ShowPage(Base):

    def __init__(self):
        """初始化Base类init"""
        super().__init__()

    def click_font(self):
        """选择字体方法"""
        # 点击字体
        self.click_ele(PageElements.setting_font_dx_xpath)
        # 点击普通
        self.click_ele(PageElements.setting_choice_pt_xpath)

    def get_summary_list(self):
        """获取页面所有的描述信息方法"""
        results = self.search_eles(PageElements.search_result_ids)
        # 获取返回值,使用列表推导式
        return [i.text for i in results]