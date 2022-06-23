# __author:lenovo
# date:2022/6/16
from appium.webdriver.common.appiumby import AppiumBy

from base.base_page import BasePage
from page.address_list_page import AddressListPage


class MainPage(BasePage):
    def goto_addresslist(self):
        # 点击通讯录
        # 1. 进入【通讯录】页面
        self.find_and_click(AppiumBy.XPATH, "//*[@text='通讯录']")
        return AddressListPage(self.driver)

    def goto_workbench(self):
        self.find_and_click(AppiumBy.XPATH, "//*[@text='工作台']")
        from page.workbench_page import WorkbenchPage
        return WorkbenchPage(self.driver)