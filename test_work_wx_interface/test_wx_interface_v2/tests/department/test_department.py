# __author:lenovo
# date:2022/7/22
import pytest
"""
编写具体的测试
用例
"""

from test_wx_interface_v2.apis.department.department import Department


class TestDepartment:

    def setup_class(self):
        self.depart = Department()  # 实例化一个对象
        self.create_data = {
            "name": "研发",
            "name_en": "YF",
            "parentid": 1,
            "order": 1,
            "id": 201
        }
        self.update_data = {
            "id": 201,
            "name": "new"+self.create_data.get("name") ,
            "name_en": "new"+self.create_data.get("name_en"),
            "parentid": 1,
            "order": 1
        }


    def test_depart_flow(self):
        # 部门新增
        creat_data = self.depart.create(self.create_data)
        # 获取部门列表，判断是否新增成功
        _list = self.depart.get()
        assert creat_data.json().get("id") in [d.get("id") for d in _list.json().get("department")]

        # 更新部门信息
        self.depart.update(self.update_data)
        _list = self.depart.get()

        assert self.update_data.get("name") in [d.get("name") for d in _list.json().get("department")]
        # 删除部门信息
        self.depart.delete(self.create_data.get("id"))
        _list = self.depart.get()
        assert self.create_data.get("id") not in [d.get("id") for d in _list.json().get("department")]
