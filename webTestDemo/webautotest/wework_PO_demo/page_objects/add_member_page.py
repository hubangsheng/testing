from selenium.webdriver.common.by import By

from webTestDemo.webautotest.wework_PO_demo.page_objects.base_page import BasePage
from webTestDemo.webautotest.wework_PO_demo.utils.log_utils import logger


class AddMemberPage(BasePage):
    __INPUT_USER_NAME = (By.NAME, 'username')
    __INPUT_USER_ACCTID = (By.NAME, 'acctid')
    __INPUT_USER_MOBILE = (By.ID, "memberAdd_phone")
    __BTN_SAVE = (By.XPATH, '//*[text()="保存"]')

    def fill_in_info(self, username, acctid, mobile):
        logger.info("填写信息")
        self.do_send_keys(username, self.__INPUT_USER_NAME)
        self.do_send_keys(acctid, self.__INPUT_USER_ACCTID)
        self.do_send_keys(mobile, self.__INPUT_USER_MOBILE)
        self.do_find(self.__BTN_SAVE).click()
        # self.driver.find_element(By.NAME, 'username').send_keys(username)
        # self.driver.find_element(By.NAME, 'acctid').send_keys(acctid)
        # self.driver.find_element(By.ID, "memberAdd_phone").send_keys(mobile)
        # self.driver.find_element(By.XPATH, '//*[text()="保存"]').click()

        from webTestDemo.webautotest.wework_PO_demo.page_objects.contact_page import ContactPage
        return ContactPage(self.driver)