from selenium.webdriver.common.by import By

from wework_PO_demo.page_objects.base_page import BasePage
from wework_PO_demo.utils.log_utils import logger


class HomePage(BasePage):
    __BTN_ADD = (By.LINK_TEXT, '添加成员')

    def click_add(self):
        logger.info("点击首页的添加成员按钮")
        self.do_find(self.__BTN_ADD).click()
        from wework_PO_demo.page_objects.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)
