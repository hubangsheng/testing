# __author:lenovo
# date:2022/7/19
from beginner.test_litemall import base64_addpassword_demo


class TestApiRequest:
    req_data = {
        "method": "get",
        "url": "http://127.0.0.1:9999/demo.txt",
        "headers": None,
        "encoding": "base64"
    }

    def test_send(self):
        ar = base64_addpassword_demo.ApiRequest()
        ar.send(self.req_data)
