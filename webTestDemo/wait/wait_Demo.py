import time

from selenium.webdriver.support.wait import WebDriverWait

if __name__ == '__main__':
    driver = "aaa"
    def fake_conditions(driver):
        print("当前时间为：", time.time())

        # until 传入的参数为一个函数对象，不是函数调用
    WebDriverWait(driver, 10, 2).until(fake_conditions, "霍格沃兹测试开发")