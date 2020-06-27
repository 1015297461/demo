from appium import webdriver


class Driver:
    # 声明app的驱动对象
    app_driver = None

    @classmethod
    def get_app_driver(cls):
        """声明手机驱动对象"""
        if cls.app_driver is None:      # 如果app_driver为None
            desired_caps = {
                'platformName': 'Android',
                'platformVersion': '5.1',
                'deviceName': 'sanxing',
                'appPackage': 'com.android.settings',
                'appActivity': '.Settings'
            }
            # 声明我们的driver对象
            cls.app_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            # 返回驱动对象
            return cls.app_driver
        return cls.app_driver

    @classmethod
    def quit_app_driver(cls):
        """退出手机驱动对象"""
        if cls.app_driver:
            # 退出
            cls.app_driver.quit()
            # 重新将app_driver置为None
            cls.app_driver = None