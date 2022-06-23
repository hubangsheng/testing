# __author:lenovo
# date:2022/6/16
from appium.webdriver.common.appiumby import AppiumBy

from base.base_page import BasePage
from page.add_member_page import AddMemberPage


class EditMemeberPage(BasePage):
    def edit_member(self, name, phonenum):
        # input name
        # input phone number
        # click ok
        self.find_and_send(AppiumBy.XPATH, "//*[contains(@text,'姓名' )]/../*[@text='必填']", name)
        # 5. 输入【手机号】
        self.find_and_send(AppiumBy.XPATH, '//*[contains(@text,"手机" )]/..//android.widget.EditText', phonenum)
        # 6. 点击【保存】
        self.find_and_click(AppiumBy.XPATH, "//*[@text='保存']")

        return AddMemberPage(self.driver)