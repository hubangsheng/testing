from appium.webdriver.common.appiumby import AppiumBy

from page_object.base_page import BasePage


class ContactPage(BasePage):
    __ADD_CONTACT = (AppiumBy.XPATH, "//*[@text='添加成员']")

    def add_user(self):
        self.swipe_find(self.__ADD_CONTACT).click()
        from page_object.home_page import HomePage
        return HomePage()
