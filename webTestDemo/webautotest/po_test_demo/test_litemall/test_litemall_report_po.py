import time

import allure
import pytest
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
    @pytest.mark.parametrize("category_name", ["a", "b", "c"])
    def test_add_type(self, category_name):
        """系统首页：进入商品类目"""
        """类目列表页：点击添加"""
        """创建类目页面：创建类目"""
        """类目列表页：获取操作结果"""
        list_page = self.home\
            .go_to_category()\
            .click_add()\
            .create_category(category_name)
        res = list_page.get_operate_result()
        assert "创建成功" == res
        # 数据清理动作，一定要放在断言之后，免得影响测试结果
        list_page.delete_category(category_name)

#     删除功能
    @pytest.mark.parametrize("category_name", ["delA", "delB", "delC"])
    def test_delete_type(self, category_name):
        res = self.home\
            .go_to_category()\
            .click_add()\
            .create_category(category_name)\
            .delete_category(category_name)\
            .get_delete_result()
        assert "删除成功" == res

