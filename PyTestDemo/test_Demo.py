import pytest


def setup_module():
    print("模块级别的setup，执行开始。。。。。")


def teardown_module():
    print("模块级别的teardown，执行结束。。。。。")


def setup_function():
    print("用例级别的setup，每个用例执行开始都会执行。。。。。")


def teardown_function():
    print("用例级别的teardown，每个用例执行结束都会执行。。。。。")

def setup():
    print("这是一个类下的用例，执行开始.......")
def teardown():
    print("这是一个类下面的用例，执行结束.........")

class TestClassDemo:
    def test_int(self):
        assert 1 == 1
    def test_float(self):
        assert 2.0 == 2.0


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4


def test_str():
    assert "abc" in "abcd"


search_list = ["appium", "selenium", "pytest"]


# 单参数的情况
@pytest.mark.parametrize("name", search_list)
def test_mark(name):
    assert name in search_list


# 多参数的情况
# 1、参数化的名字，要与方法中的参数名一一对应
# 2、如果传递多个参数的话，要放在列表中，列表中嵌套列表/元组
# 3、ids的个数，跟参数列表中的个数要相等
@pytest.mark.parametrize("test_input,expected",
                         [("3+5", 8), ("2+5", 7), ("7+5", 12)],
                         ids=["number1", "number2", "number3"])
def test_mark_more(test_input, expected: object):
    # eval 可以将字符串中的 表达式进行执行
    assert eval(test_input) == expected


# 参数化：笛卡尔积
@pytest.mark.parametrize("wd", ["appium", "selenium", "pytest"])
@pytest.mark.parametrize("code", ["utf-8", "gbk", "gb2312"])
def test_dkej(wd, code):
    print(f"wd:{wd},code:{code}")
