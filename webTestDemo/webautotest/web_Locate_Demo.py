import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_web_locate():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    # ID定位
    def test_web_locate_ID(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study")
        print("ID定位开始")
        web_element_ID = self.driver.find_element(By.ID, "locate_id")
        web_element_ID.click()
        time.sleep(2)

    # Name定位
    def test_web_locate_Name(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study")
        print("Name定位开始")
        web_element_Name = self.driver.find_element(By.NAME, "locate")
        web_element_Name.click()

    # CSS和XPATH两种定位方法需要重点掌握，熟练使用，UI自动化测试中会经常用到
    # CSS样式定位
    def test_web_locate_Css(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study")
        print("CSS选择器定位")
        web_element_CSS = self.driver.find_element(By.CSS_SELECTOR, "#locate_id > a > span")
        web_element_CSS.click()

    # Xpath定位
    def test_web_locate_xpath(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study")
        print("CSS选择器定位")
        web_element_XPATH = self.driver.find_element(By.XPATH, '//*[@id="locate_id"]/a/span')
        web_element_XPATH.click()

    # link_text定位
    def test_web_locate_Link_Text(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study")
        print("CSS选择器定位")
        web_element_Link_Text = self.driver.find_element(By.LINK_TEXT, '元素定位')
        web_element_Link_Text.click()
        time.sleep(3)

    # 常见控件交互方法
    def test_element_interaction(self):
        self.driver.get("https://www.sogou.com/")
        # 找到搜狗页面的搜索框，然后输入“霍格沃兹测试开发”
        self.driver.find_element(By.ID,"query").send_keys("霍格沃兹测试开发")
        time.sleep(2)
        # 清空输入的内容
        self.driver.find_element(By.ID,"query").clear()
        time.sleep(2)
        # 重新输入内容：上海疫情
        self.driver.find_element(By.ID,"query").send_keys("上海疫情")
        time.sleep(2)
        # 点击搜索框后面的搜狗搜索按钮
        self.driver.find_element(By.ID,"stb").click()
        time.sleep(5)

    # 获取元素属性
    def test_element_get_attr(self):
        # 1、实例化driver   这个已经在setup_method中完成了
        # 2、打开测试网页
        self.driver.get("https://vip.ceshiren.com/#/ui_study")
        # 3、定位一个元素
        web_element = self.driver.find_element(By.ID, "locate_id")
        # 4、打印这个元素对象
        # 断点打在想看的对象的下一行
        print(web_element)
        # 5、获取元素的文本信息
        # 不是每个元素都含有文本信息的
        print(web_element.text)
        # 6、获取元素的属性信息
        res = web_element.get_attribute("id")
        print(res)


