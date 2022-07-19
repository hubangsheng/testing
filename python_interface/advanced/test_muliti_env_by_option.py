# __author:lenovo
# date:2022/7/19
# 这是一个演示多环境切换的实例：通过设置命令行参数获取测试环境
import os

import requests
import yaml

from advanced.conftest import global_env

'''
编写 conftest.py  配置文件，

完成环境变量设置后，在终端中使用 pytest 命令执行一下测试脚本
pytest ./test_muliti_env_by_option.py --env=test   运行测试环境
'''


class TestMulitiEnvByOption:
    def setup_class(self):
        # 目的：在接口用例中只指定 path，不指定 url
        # 第二种方式：从命令行参数中获取测试环境
        path_env = global_env.get("env")

        # 1、读取yaml文件
        env = yaml.safe_load(open(f"{path_env}.yaml", encoding="utf-8"))
        self.base_url = env["base_url"]

    # 编写测试用例
    def test_devenv(self):
        """
        验证：是否为开发环境
        :return:
        """
        path = "get"
        r = requests.get(self.base_url + path)

        # 假设 httpbin.ceshiren.com是开发环境，那么就是断言，当前的请求是否向开发环境发起的
        assert r.json()["headers"]["Host"] == "httpbin.ceshiren.com"

    # 测试环境
    def test_testenv(self):
        path = "get"
        r = requests.get(self.base_url + path)
        assert r.json()["headers"]["Host"] == "httpbin.org"
