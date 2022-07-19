# __author:lenovo
# date:2022/7/19

# 这是一个加密解密的实例
# 文件加密
'''
1、环境准备：
    1.1 创建一个demo.json文件
    1.2 使用 base64 demo.json >demo.txt 命令对文件内容进行加密
    1.3 创建 demo 目录，用于放置加密后的文件  mkdir demo
    1.4 将加密的文件 demo.txt 移动到新的 demo 目录  mv demo.txt demo
    1.5 进入到加密文件 demo.txt 所在的目录 demo   cd demo
    1.6 执行 python -m http.server 9999  命令，使用python起一个server服务
    1.7 浏览器访问 127.0.0.1:9999 查看加密的文件内容

    ------至此，加密环境已准备好
'''


# 解密代码
import base64
import json

import requests


def test_encode():
    url = 'http://127.0.0.1:9999'
    r = requests.get(url=url)

    # r.content 表示获取一个二进制数据
    # json.loads对接口数据进行处理， json.load 对文件进行处理
    res = json.loads(base64.b64encode(r.content))
    print(res)

# 封装不同算法的解密方法
class ApiRequest:


    def send(self,data:dict):
        res = requests.request(data["method"],data["url"],headers=data["header"])
        if data["encoding"] == "base64":
            return json.loads(base64.b64encode(res.content))

        # 如果加密方法不是base64 而是第三方服务，就把加密过后的响应值发给第三方服务，让第三方去做解密，然后返回解密后的信息
        elif data["encoding"] == "private":
            return requests.post("url", data=res.content)