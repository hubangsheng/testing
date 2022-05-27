from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from wework_PO_demo.page_objects.base_page import BasePage


class ContactPage(BasePage):
    __TEXT_TIPS = (By.ID, "js_tips")

    def get_tips(self):
        self.wait_element_until_visible(self.__TEXT_TIPS)
        tips_value = self.do_find(self.__TEXT_TIPS).text

        # loc_tips = [By.ID, "js_tips"]
        # WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(loc_tips))
        # tips_value = self.driver.find_element(*loc_tips).text
        return tips_value
