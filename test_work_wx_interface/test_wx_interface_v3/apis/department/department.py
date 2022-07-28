# __author:lenovo
# date:2022/7/22
import os

import requests

from test_wx_interface_v3.utils.yaml_utils import Utils

from test_wx_interface_v3.apis.wework import WeWork

"""
封装业务层的具体实现
"""


class Department(WeWork):
    """
    接口实现：只描述接口信息，不要做断言等
    """

    '''
    设置临时环境变量
    windows 
    cmd窗口  set test_env=dev       后面的 dev 表示yaml文件中环境字段的值,或者yaml文件的名称
    powershell窗口  $env:test_env="dev"
    mac export interface_env=test

    完成环境变量设置后，在终端中使用 pytest 命令执行一下测试脚本
    '''

    def __init__(self):
        super().__init__()
        path = os.sep.join([Utils.get_frame_root_path(), "config/secrets.yaml"])
        yaml_data = Utils.get_yaml_data(path)
        corpid = yaml_data.get("corpid").get("yinian")
        secret = yaml_data.get("secret").get("contact")
        _env = os.getenv("test_env")
        self.BASE_URL = yaml_data.get(_env).get("BASE_URL")
        self.get_token(corpid, secret)



    def create(self, create_date):
        """
        创建部门
        :return:
        """

        create_url = "department/create"
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
        update_url = "department/update"
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
        delete_url = "department/delete"
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
        select_url = "department/list"
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
