import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appAutoTest.page_object.base_page import BasePage
from appAutoTest.utils.contact_info import ContactInfo

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

    # until 等到某个元素出现
    # until_not 等到某个元素消失
    # 隐式等待 + 显示等待的时候，隐式等待和显示等待会同时被触发
    # 解决方法，可以临时性的更改一下隐式等待的时长，待显示等待结束后再更改回来
    # 隐式等待什么时候会被触发？？？  当你调用find_element()的时候

    def wait_text_show(self, text):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.text_to_be_present_in_element((AppiumBy.XPATH, f"//*[@text='{text}']"), text))

    def wait_disappear(self, locator):
        self.driver.implicitly_wait(3)  # 临时更改隐式等待的时长
        WebDriverWait(self.driver, 5).until_not(lambda x: x.find_element(*locator))
        self.driver.implicitly_wait(self.implicitly_wait_time)  # 显示等待执行结束后再将隐式等待时间设置回来

    def test_delete_contact(self):
        '''
        作业要求：删除成员操作
        步骤：
        1、打开【企业微信】app
        2、进入【通讯录】页面
        3、点击右上角的搜索图标，进入搜索页面
        4、输入搜索内容（已添加的联系人姓名）
        5、点击展示的第一个联系人(有可能多个)，进入联系人详情页面
        6、点击右上角三个点，进入个人信息页面
        7、点击【编辑成员】进入编辑成员页面
        8、点击【删除成员】并确定

        验证点：
        搜索结果页面联系人不存在
        :return:
        '''

        del_contact = 'aa'
        # 1、点击【通讯录】菜单
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='通讯录']").click()
        # 2、点击通讯录页面右上角的搜索按钮
        '''
        元素定位方法：Xpath扩展用法:
        following-sibling   兄弟节点（选取当前节点之后的所有）
        preceding-sibling   兄弟节点（选取当前节点之前的所有同级节点）
        '''
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='小佛IOS科技']/../../../following-sibling::*/*[1]").click()
        # 3、输入搜索内容
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='搜索']").send_keys(del_contact)
        # 获取搜索的结果
        result = self.wait_text_show('联系人')
        print(result)

        # 无搜索结果
        if not result:
            pytest.xfail(f"无搜索结果：{del_contact}")

        # 有搜索结果
        del_contact_locator = (AppiumBy.XPATH, f"//*[@text='联系人']/../following-sibling::*//*[@text='{del_contact}']")
        # 搜索结果页面，根据页面中不变的内容查找搜索到的内容：//*[@text='联系人']/../following-sibling::*//*[@text='aa']
        # 个人信息页面右上角三个点：//*[@text='个人信息']/../../../../following-sibling::*[1]
        # 4、点击搜索按钮
        self.driver.find_element(*del_contact_locator).click()
        # 5、个人信息页点击右上角三个点按钮
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='个人信息']/../../../../following-sibling::*[1]").click()
        # 6、点击【编辑成员】按钮
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='编辑成员']").click()
        # 7、滑动查找【删除成员】按钮
        self.swipe_find('删除成员').click()
        # 8、点击【确定】按钮
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='确定']").click()
        # 重要：验证 删除是否成功
        # 等待某个元素消失，相当于断言
        self.wait_disappear(del_contact_locator)

