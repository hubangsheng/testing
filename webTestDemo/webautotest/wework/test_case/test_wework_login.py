import time

import yaml
from selenium import webdriver


class TestWeworkLogin:
    def setup_class(self):
        self.driver = webdriver.Chrome()

    def teardown_class(self):
        # self.driver.quit()
        pass

    def test_save_cookies(self):
        # 1、访问登录页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        # 2、手工扫码（直接等待）
        time.sleep(10)
        # 3、获取浏览器cookies
        cookies = self.driver.get_cookies()
        print(cookies)
        # 4、保存cookies
        with open("../data/cookies.yaml", "w") as f:
            yaml.safe_dump(data=cookies, stream=f)

    def test_get_cookie(self):
        """
        植入cookie
        """
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