# __author:lenovo
# date:2022/7/22
import requests

from test_wx_interface_v3.utils.log_utils import logger


class BaseApi:
    """
    重新封装具体的底层方法
    """
    BASE_URL = ""

    def send_api(self, req):
        """
        对requests进行二次封装
        :return: 接口对应的数据
        """
        if self.BASE_URL:
            req["url"] = self.BASE_URL+req.get("url")
        logger.info(f"发起接口请求收到的请求数据为:{req}")
        return requests.request(**req)
