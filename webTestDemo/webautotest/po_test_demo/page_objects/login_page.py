"""登录页面"""
from selenium.webdriver.common.by import By

from po_test_demo.page_objects.base_page import BasePage
from po_test_demo.utils.log_utils import logger


class LoginPage(BasePage):
    """登录页面：用户登录"""
    _BASE_URL = "http://litemall.hogwarts.ceshiren.com"
    __INPUT_USERNAME = (By.NAME, "username")
    __INPUT_PASSWORD = (By.NAME, "password")
    __BTN_LOGIN = (By.CSS_SELECTOR, ".el-button--primary")

    def login(self):
        logger.info("访问登录页面")

        # 输入”用户名“
        # self.driver.find_element(By.NAME, "username").clear()
        # self.driver.find_element(By.NAME, "username").send_keys("manage")
        # 对上面两句代码进行封装
        self.do_send_keys("manage", self.__INPUT_USERNAME)

        # 输入”密码“
        # self.driver.find_element(By.NAME, "password").clear()
        # self.driver.find_element(By.NAME, "password").send_keys("manage123")
        self.do_send_keys("manage123", self.__INPUT_PASSWORD)

        # 点击“登录”按钮
        # self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary").click()
        self.do_find(self.__BTN_LOGIN).click()

        # 此处的导入一定要导入到本地，不能导入到类
        from po_test_demo.page_objects.home_page import HomePage
        # 把创建好的实例self.driver传给页面，这样可以放置重复打开浏览器
        # ==>首页
        return HomePage(self.driver)