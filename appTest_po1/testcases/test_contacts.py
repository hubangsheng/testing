# __author:lenovo
# date:2022/6/16
from appTest_po1.base.app import App
from appTest_po1.utils.contact_info import ContactInfo


class TestContacts:
    def setup_class(self):
        self.app = App()

    def setup(self):
        # self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.back()

    def teardown_class(self):
        self.app.quit()

    def test_addcontact(self):
        name = ContactInfo.get_name()
        phonenum = ContactInfo.get_phonenum()

        result = self.main.goto_addresslist().\
            goto_addmember_page().click_addmember_menual().\
            edit_member(name, phonenum).get_text()
        assert '添加成功' == result