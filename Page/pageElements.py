from selenium.webdriver.common.by import By


class PageElements:
    """管理页面的所有元素,以页面为单位定义每一个页面类"""

    # ----------搜索页面元素----------
    # 搜索输入框
    search_input_id = (By.ID, "android:id/search_src_text")
    # 搜索结果
    search_result_ids = (By.ID, "com.android.settings:id/title")

    # ----------显示页面元素----------
    # 字体大小
    setting_font_dx_xpath = (By.XPATH, "//*[contains(@text,'字体大小')]")
    # 普通
    setting_choice_pt_xpath = (By.XPATH, "//*[contains(@text,'普通')]")
    # 描述信息
    setting_get_summary_ids = (By.ID, "android:id/summary")

    # ----------设置页面----------
    # 显示
    setting_show_btn_xpath = (By.XPATH, "//*[contains(@text,'显示')]")
    # 搜索按钮
    search_btn_id = (By.ID, "com.android.settings:id/search")

