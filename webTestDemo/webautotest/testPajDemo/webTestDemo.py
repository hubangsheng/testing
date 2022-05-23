import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLitemall:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("http://litemall.hogwarts.ceshiren.com")
        self.driver.find_element(By.NAME, "username").clear()
        self.driver.find_element(By.NAME, "username").send_keys("manage")
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "password").send_keys("manage123")
        # 点击登录按钮
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary").click()

    def teardown_class(self):
        self.driver.quit()


    def test_add_type(self):
        self.driver.maximize_window()
        # 点击商场管理/商品类目，进入商品类目页面
        self.driver.find_element(By.XPATH, "//*[text()='商场管理']").click()
        self.driver.find_element(By.XPATH, "//*[text()='商品类目']").click()

        # 添加商品
        self.driver.find_element(By.XPATH, "//*[text()='添加']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-input__inner").send_keys("新增测试商品")