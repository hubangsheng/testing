# __author:lenovo
# date:2022/7/22
import requests


class BaseApi:
    """
    重新封装具体的底层方法
    """
    def __init__(self):
        pass

    def send_api(self, req):
        """
        对requests进行二次封装
        :return: 接口对应的数据
        """
        return requests.request(**req)
