
def pytest_collection_modifyitems(items):
    for item in items:
        # 测试用例收集完成时，将收集到的item的name和nodeid的中文显示
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode-escape")
