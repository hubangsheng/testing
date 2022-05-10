import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    # ActionChains 应用一、实现鼠标单击、双击和右键操作
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        elemenet_click = self.driver.find_element(By.XPATH, "//*[@value='click me']")
        elemenet_doubleclick = self.driver.find_element(By.XPATH, "//*[@value='dbl click me']")
        elemenet_rightclick = self.driver.find_element(By.XPATH, "//*[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(elemenet_click)
        action.double_click(elemenet_doubleclick)
        action.context_click(elemenet_rightclick)
        time.sleep(3)
        action.perform()
        time.sleep(3)

    # ActionChains 应用二、实现鼠标移动到某个元素上
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com")
        ele = self.driver.find_element(By.XPATH, "//*[@id='s-usersetting-top']")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        time.sleep(3)

    # ActionChains 应用三、实现鼠标拖拽元素到某个位置上，有三种方式实现
    def test_dragdrop(self):
        self.driver.get("https://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element(By.XPATH, "//*[@id='dragger']")
        drop_element = self.driver.find_element(By.XPATH, "//*[@class = 'item'][4]")
        action = ActionChains(self.driver)
        # 方式一、使用拖拽的方式
        action.drag_and_drop(drag_element,drop_element).perform()
        # 方式二、使用按住不放的方式 release 实现鼠标抬起的操作
        drop_element = self.driver.find_element(By.XPATH, "//*[@class = 'item'][2]")
        action.click_and_hold(drag_element).release(drop_element).perform()

        # 方式三、使用移动到某个元素上
        drop_element = self.driver.find_element(By.XPATH, "//*[@class = 'item'][1]")
        action.click_and_hold(drag_element).move_to_element(drop_element).release().perform()

        time.sleep(4)

    # ActionChains 应用四、模拟键盘的按键操作
    def test_keys(self):
        self.driver.get("https://sahitest.com/demo/label.htm")
        els = self.driver.find_element(By.CSS_SELECTOR, '[type="textbox"]')
        els.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        time.sleep(3)



