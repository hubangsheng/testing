# __author:lenovo
# date:2022/6/16
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.black_hande import black_wrapper
from utils.log_util import logger


class BasePage:
    implicitly_wait_time = 30
    # 弹窗黑名单列表
    # black_list = [(AppiumBy.XPATH, "//*[@text='通讯录']")]

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    # 通过装饰器的方法，在 find 方法是实现弹窗黑名单处理
    @black_wrapper
    def find(self, by, locator):
        """
        查找元素的方法
        :param by:
        :param locator:
        :return:
        """
        return self.driver.find_element(by, locator)

    # 直接修改 find 方法，实现弹窗黑名单的处理
    # def find(self, by, locator):
    #     """
    #     查找元素的方法
    #     :param by:
    #     :param locator:
    #     :return:
    #     """
    #     try:
    #         return self.driver.find_element(by, locator)
    #     except Exception as e:
    #         print("未找到元素，处理异常")
    #         for black in self.black_list:
    #             eles = self.driver.find_elements(*black)
    #             if len(eles) > 0:
    #                 eles[0].click()
    #                 # 点掉弹窗之后，还是要在当前页面继续查找原始
    #                 return self.find(by, locator)
    #         raise e

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

    def screenshot(self, name):
        """
        截图功能
        :return:
        """
        return self.driver.save_screenshot(name)

    def get_time(self):
        pass

    def set_implicitly(self, second):
        """
        设置隐式等待
        :param second:
        :return:
        """
        self.driver.implicitly_wait(second)

    def wait_text_show(self,text):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.text_to_be_present_in_element((AppiumBy.XPATH, f"//*[contains(@text, '{text}'])"), text)
        )

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