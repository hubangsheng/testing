import pytest
# fixture作用域
# 定义了登录的fixture，尽量避免用test_开头，和具体的测试用例区分开
def test_search():
    print("搜索")

def test_cart(login):
    print("购物车")

def test_order(login):
    print("下单功能")

def test_connectDB(login,connectDB):
    print("连接数据库成功")