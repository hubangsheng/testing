import time

import yaml

from wework_PO_demo.page_objects.base_page import BasePage


class LoginPage(BasePage):
    _BASE_URL = "https://work.weixin.qq.com/wework_admin/loginpage_wx"

    def save_cookies(self):
        # 1、访问登录页面

        # self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        # 2、手工扫码（直接等待）
        time.sleep(10)
        # 3、获取浏览器cookies
        cookies = self.driver.get_cookies()
        print(cookies)
        # 4、保存cookies
        with open("../data/cookies.yaml", "w") as f:
            yaml.safe_dump(data=cookies, stream=f)

    def login(self):
        """植入cookie"""
        # 1、访问企业微信首页
        self.driver.get(self._BASE_URL)
        # 2、获取本地的cookie
        with open("../data/cookies.yaml", "r") as f:
            cookies = yaml.safe_load(f)
        # print(cookies)
        # 3、植入cookie
        for ck in cookies:
            self.driver.add_cookie(ck)
        # 4、访问企业微信首页
        self.driver.get(self._BASE_URL)

        from wework_PO_demo.page_objects.home_page import HomePage
        return HomePage(self.driver)
