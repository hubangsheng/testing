from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# driver.quit()
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestDemo():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_sogou(self):
        # 打开网页，设置窗口
        self.driver.get("https://www.sogou.com")
        self.driver.set_window_size(1233, 693)
        self.driver.find_element(By.ID, "query").click()
        self.driver.find_element(By.ID, "query").send_keys("霍格沃兹测试开发")
        # 点击搜索
        self.driver.find_element(By.ID, "stb").click()
        element = self.driver.find_element(By.ID,"stb")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        res_element = self.driver.find_element(By.CSS_SELECTOR,"#sogou_vr_30000000_0 > em")
        assert res_element.text == "霍格沃兹测试开发"
        # 浏览器控制
        self.driver.maximize_window()   #最大化浏览器窗口
        self.driver.minimize_window()   #最小化浏览器窗口
        self.driver.get("URL")          #打开URL
        self.driver.refresh()           #刷新当前页面
        self.driver.back()              #后退
        
