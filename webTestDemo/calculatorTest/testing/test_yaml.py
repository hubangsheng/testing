import yaml


def test_yaml():
    # safe_load: 把yaml格式转成python对象
    # safe_dump: 把python对象 转成yaml格式
    with open("../demo.yaml",encoding="utf-8") as f:
        result = yaml.safe_load(f)
        print(result)
