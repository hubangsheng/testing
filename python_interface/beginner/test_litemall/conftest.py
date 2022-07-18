# __author:lenovo
# date:2022/7/18

from typing import List
import pytest
import sys

sys.dont_write_bytecode = True

# 用于解决使用 pytest.mark.parametrize 对用例进行参数化的时候，传入的值包含中文，运行用例，控制台显示编码问题
def pytest_collection_modifyitems(session: "Session", config: "Config", items: List["Item"]) -> None:
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")
