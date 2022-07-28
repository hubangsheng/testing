# __author:lenovo
# date:2022/7/22
import requests

from test_wx_interface_v3.apis.base_api import BaseApi


class WeWork(BaseApi):
    """
    用例执行前的数据准备，如这里的token数据
    """
    def __init__(self):
        self.access_token = None

    def get_token(self, corpid, secret):
        """
        获取token
        :return:
        """
        url = "gettoken"

        params = {
            "corpid": corpid,
            "corpsecret": secret
        }
        req = {
            "method": "GET",
            "url": url,
            "params": params
        }
        # 发起接口请求
        # r = requests.request("GET", url=url, params=params)
        # r = requests.get(url=url, params=params)
        r = self.send_api(req)
        # 提取token
        self.access_token = r.json().get("access_token")
        # return token
