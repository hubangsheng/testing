# __author:lenovo
# date:2022/7/22
import requests

from test_wx_interface_v2.apis.base_api import BaseApi


class WeWork(BaseApi):
    # access_token = ""
    """
    用例执行前的数据准备，如这里的token数据
    """

    def __init__(self):
        super().__init__()
        self.access_token = self.get_token()

    def get_token(self):
        """
        获取token
        :return:
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid": "wwb1241eeac52c8c3e",
            "corpsecret": "acXBLGT4cNPcm0jIfNPtleWhR6Gz-Jym9B99do8NOwQ"
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
        token = r.json().get("access_token")
        return token
