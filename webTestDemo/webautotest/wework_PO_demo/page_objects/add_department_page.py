from selenium.webdriver.common.by import By

from webTestDemo.webautotest.wework_PO_demo.page_objects.base_page import BasePage


class AddDepartmentPage(BasePage):
    __INPUT_DEPARTMENT_MSG = (By.NAME, "name")
    __BTN_CHANGE_DEPARTMENT = (By.XPATH, '//*[text()="选择所属部门"]')
    __CHANGE_DEPARTMENT = (By.XPATH, "//div[@class='inputDlg_item']//a[text()='小佛IOS科技']")
    __BTN_OK = (By.XPATH, '//*[text()="确定"]')
    def click_OK(self):
        self.do_send_keys("IT", self.__INPUT_DEPARTMENT_MSG)
        self.do_find(self.__BTN_CHANGE_DEPARTMENT).click()
        self.do_find(self.__CHANGE_DEPARTMENT).click()
        self.do_find(self.__BTN_OK).click()



        # self.driver.find_element(By.NAME, "name").send_keys("信息")
        # self.driver.find_element(By.XPATH, '//*[text()="选择所属部门"]').click()
        # self.driver.find_element(By.XPATH, "//div[@class='inputDlg_item']//a[text()='小佛IOS科技']").click()
        # self.driver.find_element(By.XPATH, '//*[text()="确定"]').click()
        # loc_tips = [By.ID, "js_tips"]
        # WebDriverWait(self.driver, 10, 2).until(expected_conditions.visibility_of_element_located(loc_tips))
        # tips_value = self.driver.find_element(*loc_tips).text

        from webTestDemo.webautotest.wework_PO_demo.page_objects.department_page import DepartmentPage
        return DepartmentPage(self.driver)


