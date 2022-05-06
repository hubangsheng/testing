from selenium import webdriver
from selenium.webdriver.common.by import By

'''
一、测试对象：
    1、测试人网站上的搜索功能

二、演练代码中包含的知识点：
    1、使用 setup/teardown 完成用例前置条件的准备和测试结束后的收尾工作
    2、使用 implicitly_wait() 隐式等待
    3、使用 CSS 定位技术对测试对象进行定位
'''

class TestCeshiren:
    def setup(self):
        self.driver = webdriver.Chrome()
        # self.vars = {}
        self.driver.implicitly_wait(5)
        self.driver.get("https://ceshiren.com/search?expanded=true")
        print("初始化数据内容完毕.....")

    def teardown(self):
        self.driver.quit()
        print("测试结束......")

    def test_search(self):
        # 定位到搜索输入框，并输入准备的数据
        self.driver.find_element(By.CSS_SELECTOR, "[placeholder='搜索']").send_keys("appium")
        # 定位搜索按钮，并点击
        self.driver.find_element(By.CSS_SELECTOR, ".search-cta").click()
        web_element = self.driver.find_element(By.CSS_SELECTOR, ".topic-title")
        # 这里的text属性是可以通过对测试代码打断点调试的时候看到
        # 获取文本类的实际结果，
        print(web_element.text)
        # 断言，appium关键字是否在获取的文本结果之中
        '''
        两种解决方案：
        1、统一、比如 断言 Appium in
        2、就是把获取到的内容和预期结果统一，使用 .lower() 方法就可以使大写的字母小写
        '''
        assert "appium" in web_element.text.lower()
