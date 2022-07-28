# __author:lenovo
# date:2022/7/22
import os

import allure
import jsonpath as jsonpath

from test_wx_interface_v3.apis.department.department import Department

"""
编写具体的测试用例
"""


@allure.feature("部门管理")
class TestDepartment:

    def setup_class(self):
        # path = os.sep.join([Utils.get_frame_root_path(), "config/secrets.yaml"])
        # yaml_data = Utils.get_yaml_data(path)
        # corpid = yaml_data.get("corpid").get("yinian")
        # secret = yaml_data.get("secret").get("contact")
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
            "name": "new" + self.create_data.get("name"),
            "name_en": "new" + self.create_data.get("name_en"),
            "parentid": 1,
            "order": 1
        }
    @allure.story("测试流程")
    def test_depart_flow(self):
        # 部门新增
        with allure.step("创建部门"):
            creat_data = self.depart.create(self.create_data)
            # 获取部门列表，判断是否新增成功
            _list = self.depart.get()
            # assert creat_data.json().get("id") in [d.get("id") for d in _list.json().get("department")]
            # 使用 jsonpath 实现取指定字段的值并放置在列表中
            assert creat_data.json().get("id") in jsonpath.jsonpath(_list.json(), "$..id")

        # 更新部门信息
        with allure.step("更新部门"):
            self.depart.update(self.update_data)
            _list = self.depart.get()
            # assert self.update_data.get("name") in [d.get("name") for d in _list.json().get("department")]
            assert self.update_data.get("name") in jsonpath.jsonpath(_list.json(), "$..name")

        # 删除部门信息
        with allure.step("删除部门"):
            self.depart.delete(self.create_data.get("id"))
            _list = self.depart.get()
            # assert self.create_data.get("id") not in [d.get("id") for d in _list.json().get("department")]
            assert self.create_data.get("id") not in jsonpath.jsonpath(_list.json(), "$..id")
