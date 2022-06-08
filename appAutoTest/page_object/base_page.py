from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

from utils.log_util import logger


class BasePage:
    implicitly_wait_time = 30

    def setup(self):
        # 资源初始化
        # 打开【企业微信】应用
        caps = {}
        caps["platformName"] = "Android"
        # mac: adb logcat ActivityManager:I | grep "cmp"
        # windows:adb logcat ActivityManager:I | findstr "cmp"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # adb devices
        caps["deviceName"] = "M2002J9E"
        # "True" 是绝对不可以的  要么是"true" 要么是 True
        # 防止清缓存
        caps["noReset"] = "true"
        # 动态页面等待0秒 再去查找元素， 默认是等待10秒
        caps["settings[waitForIdleTimeout]"] = 0
        # 创建driver ,与appium server建立连接，返回一个 session
        # driver 变成self.driver 由局部变量变成实例变量，就可以在其它的方法中引用这个实例变量了
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 隐式等待是全局的等待方式
        self.driver.implicitly_wait(self.implicitly_wait_time)

    def teardown(self):
        pass

    def swipe_find(self, text, num=3):
        # 自定义滑动查找，
        self.driver.implicitly_wait(1)
        for i in range(num):
            try:
                element = self.driver.find_element(AppiumBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(self.implicitly_wait_time)
                return element
            except:
                logger.info("未找到元素，开始滑动")
                # 获取当前屏幕尺寸
                # 'width', 'height'
                size = self.driver.get_window_size()
                width = size.get("width")
                height = size.get("height")
                logger.info(f"当前屏幕的宽：{width}, 高：{height}")
                start_x = width / 2
                start_y = height * 0.8
                end_x = start_x
                end_y = height * 0.3
                duration = 1000
                logger.info("开始滑动")
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)
            if i == num - 1:
                self.driver.implicitly_wait(self.implicitly_wait_time)
                raise NoSuchElementException(f"找了{num}次 ，未找到元素{text}")

    def do_find(self, by, locator=None):
        if locator:
            return self.driver.find_element(by, locator)
        else:
            return self.driver.find_element(*by)

    def do_finds(self, by, locator=None):
        if locator:
            return self.driver.find_elements(by, locator)
        else:
            return self.driver.find_elements(*by)

    def do_send_keys(self, value, by, locator=None):
        elm = self.do_find(by, locator)
        elm.clear()
        elm.send_keys(value)
