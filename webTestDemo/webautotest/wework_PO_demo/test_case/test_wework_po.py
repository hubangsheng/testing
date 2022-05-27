import time

import faker.providers.date_time
import yaml
from faker import Faker

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from wework_PO_demo.page_objects.login_page import LoginPage


class TestWeworkLogin:
    def setup_class(self):
        fake = Faker("zh_CN")
        self.username = fake.name()
        self.acctid = fake.ssn()
        self.mobile = fake.phone_number()

        # 打开登录页,实例化一个操作对象
        self.browser = LoginPage()

    def teardown_class(self):
        # self.browser.do_quit()
        pass

    def test_add_member_po(self):
        value = self.browser\
            .login()\
            .click_add()\
            .fill_in_info(self.username, self.acctid, self.mobile)\
            .get_tips()
        assert "保存成功" == value

    #
    #     self.driver = webdriver.Chrome()
    #     self.driver.implicitly_wait(5)
    #     self.driver.maximize_window()
    #     """植入cookie"""
    #     # 1、访问企业微信首页
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
    #     # 2、获取本地的cookie
    #     with open("../data/cookies.yaml", "r") as f:
    #         cookies = yaml.safe_load(f)
    #     print(cookies)
    #     # 3、植入cookie
    #     for ck in cookies:
    #         self.driver.add_cookie(ck)
    #     # 4、访问企业微信首页
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
    #
    # def teardown_class(self):
    #     self.driver.quit()
    #
    # def save_cookies(self):
    #     # 1、访问登录页面
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
    #     # 2、手工扫码（直接等待）
    #     time.sleep(10)
    #     # 3、获取浏览器cookies
    #     cookies = self.driver.get_cookies()
    #     print(cookies)
    #     # 4、保存cookies
    #     with open("../data/cookies.yaml", "w") as f:
    #         yaml.safe_dump(data=cookies, stream=f)
    #
    # def get_cookie(self):
    #     """植入cookie"""
    #     # 1、访问企业微信首页
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
    #     # 2、获取本地的cookie
    #     with open("../data/cookies.yaml", "r") as f:
    #         cookies = yaml.safe_load(f)
    #     print(cookies)
    #     # 3、植入cookie
    #     for ck in cookies:
    #         self.driver.add_cookie(ck)
    #     # 4、访问企业微信首页
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    # 从通讯录添加成员操作

    #     username = "zhangsan6"
    #     code = "123406"
    #     phone = "15380430005"
    #     # 点击首页的通讯录菜单
    #     self.driver.find_element(By.XPATH, '//*[text()="通讯录"]').click()
    #
    #     # 点击添加成员按钮
    #     self.driver.find_element(By.LINK_TEXT, '添加成员').click()
    #     # 添加成员页面输入成员名字，id和手机号并保存
    #     self.driver.find_element(By.NAME, 'username').send_keys(username)
    #     self.driver.find_element(By.NAME, 'acctid').send_keys(code)
    #     self.driver.find_element(By.ID, "memberAdd_phone").send_keys(phone)
    #     self.driver.find_element(By.XPATH, '//*[text()="保存"]').click()
    #     # 获取保存成功弹窗信息
    #     loc_tips = [By.ID, "js_tips"]
    #     WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(loc_tips))
    #     tips_value = self.driver.find_element(*loc_tips).text
    #     print(tips_value)
    #     assert "保存成功" == tips_value
    #
    #     # 删除成员
    #     # 选择指定的成员并勾选ckeckbox
    #     self.driver.find_element(By.XPATH, f'//*[text()="{username}"]/../..//*[@class="ww_checkbox"]').click()
    #     # 点击删除按钮
    #     self.driver.find_element(By.CSS_SELECTOR, '.qui_btn.ww_btn.js_delete').click()
    #     # 点击确认按钮
    #     self.driver.find_element(By.XPATH, '//*[text()="确认"]').click()
    #
    # def test_add_department(self):
    #
    #     # 从通讯录页面添加部门操作
    #     self.driver.find_element(By.XPATH, '//*[text()="通讯录"]').click()
    #     self.driver.find_element(By.CSS_SELECTOR, '.member_colLeft_top_addBtn').click()
    #     self.driver.find_element(By.XPATH, '//*[text()="添加部门"]').click()
    #     self.driver.find_element(By.NAME, "name").send_keys("信息")
    #     # self.driver.find_element(By.CSS_SELECTOR, ".qui_btn.ww_btn.ww_btn_Dropdown.js_toggle_party_list").click()
    #     self.driver.find_element(By.XPATH, '//*[text()="选择所属部门"]').click()
    #     self.driver.find_element(By.XPATH, "//div[@class='inputDlg_item']//a[text()='小佛IOS科技']").click()
    #     self.driver.find_element(By.XPATH, '//*[text()="确定"]').click()
    #     loc_tips = [By.ID, "js_tips"]
    #     WebDriverWait(self.driver, 10, 2).until(expected_conditions.visibility_of_element_located(loc_tips))
    #     tips_value = self.driver.find_element(*loc_tips).text
    #     assert "新建部门成功" == tips_value
    #
    #
    #
    #
