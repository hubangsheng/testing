from selenium.webdriver.common.by import By

from webTestDemo.webautotest.wework_PO_demo.page_objects.base_page import BasePage


class DepartmentPage(BasePage):
    __TEXT_TIPS = (By.ID, "js_tips")

    def get_department_tips(self):
        self.wait_element_until_visible(self.__TEXT_TIPS)
        tips_value = self.do_find(self.__TEXT_TIPS).text

        return tips_value
