# __author:lenovo
# date:2022/6/16
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.common import NoSuchElementException

from appTest_po1.utils.log_util import logger


class BasePage:
    implicitly_wait_time = 30

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        """
        查找元素的方法
        :param by:
        :param locator:
        :return:
        """
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        self.find(by, locator).click()

    def find_and_send(self, by, locator, text):
        self.find(by, locator).send_keys(text)

    def finds(self, by, locator):
        """
        查找多个元素
        :param by:
        :param locator:
        :return:
        """
        return self.driver.find_elements(by, locator)

    def get_toast_text(self):
        toast_text = self.find(AppiumBy.XPATH, "//*[@class='android.widget.Toast']").text
        return toast_text

    def back(self, num=1):
        for i in range(num):
            self.driver.back()

    def set_implicitly(self,second):
        """
        设置隐式等待
        :param second:
        :return:
        """
        self.driver.implicitly_wait(second)

    def get_window_size(self):
        """
        获取窗口尺寸
        :return:
        """
        return self.driver.get_window_size()

    def swipe_up(self):
        """
        向上滑动
        :return:
        """
        # 获取当前屏幕尺寸
        # 'width', 'height'
        size = self.get_window_size()
        width = size.get("width")
        height = size.get("height")
        logger.info(f"当前屏幕的宽：{width}, 高：{height}")
        start_x = width / 2
        start_y = height * 0.8
        end_x = start_x
        end_y = height * 0.3
        duration = 1000
        logger.info(f"开始滑动：{start_x},{start_y} to {end_x},{end_y}")
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def swipe_find(self, text, num=3):
        # 自定义滑动查找，
        self.set_implicitly(1)
        for i in range(num):
            try:
                element = self.find(AppiumBy.XPATH, f"//*[@text='{text}']")
                self.set_implicitly(self.implicitly_wait_time)
                return element
            except:
                logger.info("未找到元素，开始滑动")
                self.swipe_up()
            if i == num - 1:
                self.set_implicitly(self.implicitly_wait_time)
                raise NoSuchElementException(f"找了{num}次 ，未找到元素{text}")