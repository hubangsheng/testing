
# conftest.py名字是固定的
import pytest


@pytest.fixture(scope="function")
def login():
    # setup操作
    print("完成登录操作")
    token = "abcdefg"
    username = "hogwarts"
    yield token,username
    # teardown操作
    print("完成登出操作")

@pytest.fixture()
def connectDB():
    print("连接数据库")
    yield
    print("断开数据库")