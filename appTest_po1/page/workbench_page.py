# __author:lenovo
# date:2022/6/23
from appium.webdriver.common.appiumby import AppiumBy

from base.base_page import BasePage


class WorkbenchPage(BasePage):
    def clicke_mark(self):
        self.swipe_find('打卡')
        self.find_and_click(AppiumBy.XPATH, "//*[@text='完成']")
        self.find_and_click(AppiumBy.XPATH, "//*[@text='打卡']")
        from page.mar_page import MarkPage
        return MarkPage(self.driver)
