# __author:lenovo
# date:2022/7/19

# 这是一个将xml转换成dic，从而实现将xml转换为json格式，方便统一断言

# 环境中需要先安装 xmltodict 这个插件  pip install xmltodict
# 注意：xmltodict的版本必须为0.13.0以上的版本
import requests
import xmltodict


def test_xml_to_dict():
    res = requests.get("https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss")
    # 注意不是直接打印 res ,而是打印 res 的 text 属性
    # print(res.text)
    # 转换成 python标准的 dict 格式
    res_dict = xmltodict.parse(res.text)
    print(res_dict)