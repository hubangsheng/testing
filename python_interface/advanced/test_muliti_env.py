# __author:lenovo
# date:2022/7/19
# 这是一个演示多环境切换的实例：通过环境变量获取测试环境
import os

import requests
import yaml
'''
设置临时环境变量
windows 
cmd窗口  set interface_env=test       后面的 test 表示yaml文件的名称
powershell窗口  $env:interface_env="test"
mac export interface_env=test

完成环境变量设置后，在终端中使用 pytest 命令执行一下测试脚本
'''

class TestMulitiEnv:
    def setup_class(self):
        # 目的：在接口用例中只指定 path，不指定 url
        # self.base_url = "https://httpbin.ceshiren.com/"

        # 第一种方式：从环境变量读取配置名称为interface_env的配置环境
        path_env = os.getenv("interface_env")

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
