# __author:lenovo
# date:2022/7/22
import pytest
import requests


class TestWxInterface():
    def setup_class(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid": "wwb1241eeac52c8c3e",
            "corpsecret": "acXBLGT4cNPcm0jIfNPtleWhR6Gz-Jym9B99do8NOwQ"
        }

        r = requests.get(url=url, params=params)
        # print(r.json().get("access_token"))
        self.access_token = r.json().get("access_token")

    # 增加部门接口用例
    # 参数化，最后一个expect表示断言信息，此处为返回的状态码
    @pytest.mark.parametrize("name, name_en, parentid, order, _id, expect", [
        ("研发", "YF", 1, 1, 201, 0),
        ("测试", "CS", 1, 1, 301, 0),
        ("测试", "CS", 1, 1, 301, 6008),  # 重复的部门，添加失败
    ])
    def test_create(self, name, name_en, parentid, order, _id, expect):
        create_url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        create_date = {
            "name": name,
            "name_en": name_en,
            "parentid": parentid,
            "order": order,
            "id": id
        }
        params = {
            "access_token": self.access_token
        }
        r = requests.post(url=create_url, json=create_date, params=params)
        print(r.json())
        assert r.json().get("errcode") == expect and r.json().get("errmsg") == "created"

    # 更新部门信息接口测试
    def test_update(self):
        update_url = "https://qyapi.weixin.qq.com/cgi-bin/department/update"
        update_data = {
            "id": 301,
            "name": "广州研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1
        }
        params = {
            "access_token": self.access_token
        }
        update_r = requests.post(url=update_url, json=update_data, params=params)
        assert update_r.json().get("errcode") == 0 and update_r.json().get("errmsg") == "updated"

    # 删除部门接口
    @pytest.mark.parametrize("id", [201, 301])
    def test_delete(self, id):
        delete_url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
        del_data = {
            "access_token": self.access_token,
            "id": id
        }
        delete_r = requests.get(url=delete_url, params=del_data)
        assert delete_r.json().get("errcode") == 0 and delete_r.json().get("errmsg") == "deleted"

    # 查询部门列表
    def test_select_list(self):
        select_url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
        params = {
            "access_token": self.access_token
        }
        select_r = requests.get(url=select_url, params=params)
        print(select_r.json())
        assert select_r.json().get("errcode") == 0
