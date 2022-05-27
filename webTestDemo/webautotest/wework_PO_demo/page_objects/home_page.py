from selenium.webdriver.common.by import By

from wework_PO_demo.page_objects.base_page import BasePage
from wework_PO_demo.utils.log_utils import logger


class HomePage(BasePage):
    __MENU_CONTACT = (By.XPATH, '//*[text()="通讯录"]')
    __BTN_ADD = (By.LINK_TEXT, '添加成员')
    __BTN_ADD_MARK = (By.CSS_SELECTOR, '.member_colLeft_top_addBtn')
    __BTN_ADD_DEPARTMENT = (By.XPATH, '//*[text()="添加部门"]')

    def click_add_user(self):
        logger.info("点击首页的通讯录菜单")
        self.do_find(self.__MENU_CONTACT).click()
        logger.info("点击添加成员按钮")
        self.do_find(self.__BTN_ADD).click()
        from wework_PO_demo.page_objects.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)

    def click_add_department(self):
        logger.info("点击通讯录菜单")
        self.do_find(self.__MENU_CONTACT).click()

        logger.info("点击添加部门的+号按钮")
        self.do_find(self.__BTN_ADD_MARK).click()
        # 选择“添加部门”下拉列表，并点击
        self.do_find(self.__BTN_ADD_DEPARTMENT).click()

        from wework_PO_demo.page_objects.add_department_page import AddDepartmentPage
        return AddDepartmentPage(self.driver)

        # self.driver.find_element(By.CSS_SELECTOR, '.member_colLeft_top_addBtn').click()
        # self.driver.find_element(By.XPATH, '//*[text()="添加部门"]').click()
