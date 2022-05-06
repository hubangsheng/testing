import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_CSS_Demo():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.implicitly_wait(5)
        self.driver.get("https://ceshiren.com/search?expanded=true")
        print("初始化数据内容完毕.....")

    def teardown(self):
        self.driver.quit()

    def test_web_wait(self):
        self.driver.find_element(By.CSS_SELECTOR, "[placeholder='搜索']").send_keys("appium")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary.search-cta.btn.btn-icon-text.ember-view").click()
        web_element = self.driver.find_element(By.CSS_SELECTOR, ".topic-title")
        assert "appium" in web_element.text.lower()
