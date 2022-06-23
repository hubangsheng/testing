# __author:lenovo
# date:2022/6/16
import pytest

from base.app import App
from utils import operate_yaml


class TestContacts:
    contact_datas = operate_yaml.get_data("../datas/contacts.yml")

    def setup_class(self):
        self.app = App()

    def setup(self):
        # self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.back()

    def teardown_class(self):
        self.app.quit()

    @pytest.mark.parametrize('name, phonenum', contact_datas)
    def test_addcontact(self, name, phonenum):
        # name = ContactInfo.get_name()
        # phonenum = ContactInfo.get_phonenum()

        result = self.main.goto_addresslist(). \
            goto_addmember_page().click_addmember_menual(). \
            edit_member(name, phonenum).get_text()
        assert '添加成功' == result

    def test_mark(self):
        mark_msg = self.main.goto_workbench().clicke_mark().mark()
        assert '外出打卡成功' == mark_msg
