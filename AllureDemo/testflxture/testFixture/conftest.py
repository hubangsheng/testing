import time

import pytest

from testflxture.pythoncode.calculator import Calculator


def pytest_collection_modifyitems(items):
    for item in items:
        # 测试用例收集完成时，将收集到的item的name和nodeid的中文显示
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode-escape")

@pytest.fixture(scope="class")
def get_calc():
    calc = Calculator()
    yield calc
    print("测试结束")

@pytest.fixture(autouse=True)
def calc_fix():
    print("开始计算")
    yield
    print("结束计算")

# 使用这个fixture，可以对生成的日志文件按时间进行命名
@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    log_name = 'output/log/' + now + '.logs'

    request.config.pluginmanager.get_plugin("logging-plugin") \
        .set_log_path(log_name)