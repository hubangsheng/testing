# __author:lenovo
# date:2022/7/19

# 这是一个将响应体为xml的格式，转换成统一的json格式的实例
import requests
import xmltodict
from requests import Response


def test_response_to_dict():
    # 不同响应体的请求地址
    # res = requests.get("https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss")
    res = requests.get("https://httpbin.ceshiren.com/get")

    # 注意不是直接打印 res ,而是打印 res 的 text 属性
    final_res = reponse_to_dict(res)
    # 断言响应值是否为dict类型的格式
    assert isinstance(final_res,dict)


def reponse_to_dict(response: Response):
    res_text = response.text
    # 判断响应文本信息是否以 <?xml 开头
    if res_text.startswith("<?xml"):
        final_dict = xmltodict.parse(res_text)
    elif res_text.startswith("<!DOCTYPE html>"):
        final_dict = "html"
    # 如果是json 则返回json格式
    else:
        final_dict = response.json()

    return final_dict
