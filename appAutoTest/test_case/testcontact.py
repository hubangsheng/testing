import time

from appium.webdriver.common.appiumby import AppiumBy

from page_object.base_page import BasePage
from page_object.home_page import HomePage
from utils.contact_info import ContactInfo

"""
前提条件：
1、提前注册企业微信管理员帐号
2、手机端安装企业微信
3、企业微信 app 处于登录状态
"""


class TestContact(BasePage):

    def test_addcon(self):
        """
        通讯录添加成员用例步骤:
            进入【通讯录】页面
            点击【添加成员】
            点击【手动输入添加】
            输入【姓名】【手机号】并点击【保存】
        验证点：
            登录成功提示信息
        """
        # self.home = self.driver.HomePage()
        # self.home.click_Contact().add_user()

        name = ContactInfo.get_name()
        phonenum = ContactInfo.get_phonenum()
        # 1. 进入【通讯录】页面
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='通讯录']").click()
        # 2. 点击【添加成员】
        # self.driver.find_element(AppiumBy.XPATH, "//*[@text='添加成员']").click()
        self.swipe_find("添加成员").click()
        # 3. 点击【手动输入添加】
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='手动输入添加']").click()
        # 4. 输入【姓名】
        self.driver.find_element(AppiumBy.XPATH,
                                 "//*[contains(@text,'姓名' )]/../*[@text='必填']"). \
            send_keys(name)
        # 5. 输入【手机号】
        self.driver.find_element(AppiumBy.XPATH,
                                 '//*[contains(@text,"手机" )]/..//android.widget.EditText'). \
            send_keys(phonenum)
        # 6. 点击【保存】
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='保存']").click()
        # time.sleep(2)
        # print(self.driver.page_source)
        result = self.driver.find_element(AppiumBy.XPATH, "//*[@class='android.widget.Toast']").text
        # 验证点：登录成功提示信息
        assert result == "添加成功"

    def test_mark(self):
        """
        打卡功能用例步骤:
            进入【工作台】页面
            滑动找到【打卡】按钮并点击
            点击【外出打卡】tab
            点击【第N次打卡】
        验证点：
            提示外出打卡成功
        """
        # 1、进入【工作台】页面
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='工作台']").click()

        # 2、滑动找到【打卡】按钮并点击
        # __BTN_MARK = (AppiumBy.XPATH, "//*[@text='打卡']")
        self.swipe_find('打卡')
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='完成']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='打卡']").click()

        # 3、点击【外出打卡】tab
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='外出打卡']").click()

        # 4、点击【第N次打卡】
        self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text, '次外出')]").click()

        # 5、验证
        res = self.driver.find_element(AppiumBy.XPATH, "//*[@text='外出打卡成功']").text
        assert '外出打卡成功' == res

    def test_delete_contact(self):
        # 1、点击【通讯录】菜单
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='通讯录']").click()

        # 2、点击通讯录管理图标
        self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/kor']").click()

        # 获取删除成员前通讯录列表中成员的数量
        res = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text, '人未加入')]").text

        # 3、点击指定的人名进行删除操作
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='郝娟']").click()
        self.swipe_find('删除成员').click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='确定']").click()

        # 获取删除成员之后总的成员数量
        time.sleep(3)
        res_New = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text, '人未加入')]").text
        assert int(res[1])-1 == int(res_New[1])
        # print(res,res_New)


