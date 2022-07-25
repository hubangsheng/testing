# __author:lenovo
# date:2022/7/22
import requests
"""
封装业务层的具体实现
"""
from test_wx_interface_v2.apis.wework import WeWork


class Department(WeWork):
    """
    接口实现：只描述接口信息，不要做断言等
    """

    def create(self, create_date):
        """
        创建部门
        :return:
        """

        create_url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        params = {
            "access_token": self.access_token
        }
        # 组装调用send的参数
        req = {
            "method": "POST",
            "url": create_url,
            "params": params,
            "json": create_date
        }
        create_r = self.send_api(req)
        # 返回请求返回的结果
        return create_r

    def update(self, update_data):
        """
        更新部门信息
        :return:
        """
        update_url = "https://qyapi.weixin.qq.com/cgi-bin/department/update"
        params = {
            "access_token": self.access_token
        }
        req = {
            "method": "POST",
            "url": update_url,
            "params": params,
            "json": update_data
        }
        # update_r = requests.request("POST", url=update_url, json=update_data, params=params)
        update_r = self.send_api(req)
        return update_r

    def delete(self, _id):
        """
        删除部门
        :return:
        """
        delete_url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
        del_data = {
            "access_token": self.access_token,
            "id": _id
        }
        req = {
            "method": "GET",
            "url": delete_url,
            "params": del_data
        }

        # delete_r = requests.request("GET", url=delete_url, params=del_data)
        delete_r = self.send_api(req)
        return delete_r

    def get(self, _id=None):
        """
        查询部门信息
        :return:
        """
        select_url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
        params = {
            "access_token": self.access_token,
            "id": _id
        }
        req = {
            "method": "GET",
            "url": select_url,
            "params": params
        }
        # select_r = requests.request("GET", url=select_url, params=params)
        select_r = self.send_api(req)
        return select_r
