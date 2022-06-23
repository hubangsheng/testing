# __author:lenovo
# date:2022/6/23
from appium.webdriver.common.appiumby import AppiumBy

from base.base_page import BasePage


class MarkPage(BasePage):
    def mark(self):
        self.find_and_click(AppiumBy.XPATH, "//*[@text='外出打卡']")
        # self.wait_text_show('次外出')
        self.find_and_click(AppiumBy.XPATH, "//*[contains(@text, '次外出')]")

        res = self.find(AppiumBy.XPATH, "//*[@text='外出打卡成功']").text
        return res