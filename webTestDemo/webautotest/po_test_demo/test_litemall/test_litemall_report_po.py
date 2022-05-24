import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from po_test_demo.page_objects.login_page import LoginPage
from po_test_demo.utils.log_utils import logger


class TestLitemall:
    # 前置动作
    def setup_class(self):
        """登录页面：用户登录"""
        self.home = LoginPage().login()
    def teardown_class(self):
        self.home.do_quit()

    # 新增功能
    def test_add_type(self):
        """系统首页：进入商品类目"""
        """类目列表页：点击添加"""
        """创建类目页面：创建类目"""
        """类目列表页：获取操作结果"""
        res = self.home\
            .go_to_category()\
            .click_add()\
            .create_category("新增商品测试")\
            .get_operate_result()
        assert "创建成功" == res

#     删除功能
    def test_delete_type(self):
        res = self.home\
            .go_to_category()\
            .click_add()\
            .create_category("删除商品测试")\
            .delete_category("删除商品测试")\
            .get_delete_result()
        assert "删除成功" == res

