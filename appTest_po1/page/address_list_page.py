# __author:lenovo
# date:2022/6/16
from base.base_page import BasePage
from page.add_member_page import AddMemberPage


class AddressListPage(BasePage):

        def goto_addmember_page(self):
            # 点击添加成员
            # 2. 点击【添加成员】
            # self.driver.find_element(AppiumBy.XPATH, "//*[@text='添加成员']").click()

            self.swipe_find("添加成员").click()
            return AddMemberPage(self.driver)