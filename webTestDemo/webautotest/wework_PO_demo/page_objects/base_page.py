import time

import allure
import yaml
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _BASE_URL = ""

    def __init__(self, base_driver=None):
        if base_driver:
            self.driver = base_driver
        else:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()

        if not self.driver.current_url.startswith("http"):
            self.driver.get(self._BASE_URL)

    # 找单个元素
    def do_find(self, by, locator=None):
        if locator:
            return self.driver.find_element(by, locator)
        else:
            return self.driver.find_element(*by)

    # 找多个元素
    def do_finds(self, by, locator=None):
        if locator:
            return self.driver.find_elements(by, locator)
        else:
            return self.driver.find_elements(*by)

    # 向页面文本框中输入数据
    def do_send_keys(self, value, by, locator=None):
        ele = self.do_find(by, locator)
        ele.clear()
        ele.send_keys(value)

    def do_quit(self):
        self.driver.quit()

    # 植入cookie 自动登录
    def get_cookie(self):
        """植入cookie"""
        # 1、访问企业微信首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 2、获取本地的cookie
        with open("../data/cookies.yaml", "r") as f:
            cookies = yaml.safe_load(f)
        print(cookies)
        # 3、植入cookie
        for ck in cookies:
            self.driver.add_cookie(ck)
        # 4、访问企业微信首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    def get_screen(self):
        timestamp = int(time.time())
        image_path = f"./images/image_{timestamp}.PNG"
        # 截图
        self.driver.save_screenshot(image_path)
        allure.attach.file(image_path, name='picture', attachment_type=allure.attachment_type.PNG)

    def wait_element_until_visible(self, locator: tuple):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
