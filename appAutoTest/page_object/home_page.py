from appium.webdriver.common.appiumby import AppiumBy

from page_object.base_page import BasePage
from utils.log_util import logger


class HomePage(BasePage):
    __MENU_CONTACT = (AppiumBy.XPATH, "//*[@text='通讯录']")
    __MENU_WORK = (AppiumBy.XPATH, "//*[@text='工作台']")

    def click_Contact(self):
        logger.info("点击首页的通讯录菜单")
        self.do_find(self.__MENU_CONTACT).click()
        from page_object.contact_page import ContactPage
        return ContactPage()

