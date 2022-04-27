import os
import allure
import pytest

class TestSearch():
    @allure.title("搜索词为Android")
    def test_case1(self):
        print("case1")

    @allure.title("搜索词为IOS")
    def test_case2(self):
        print("case2")