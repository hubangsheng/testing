# __author:lenovo
# date:2022/6/16
from appium.webdriver.common.appiumby import AppiumBy

from base.base_page import BasePage


class AddMemberPage(BasePage):
    def click_addmember_menual(self):
        # 3. 点击【手动输入添加】
        self.find_and_click(AppiumBy.XPATH, "//*[@text='手动输入添加']")

        from page.edit_member_page import EditMemeberPage
        return EditMemeberPage(self.driver)

    def get_text(self):
        res = self.get_toast_text()
        return res