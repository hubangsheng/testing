import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

'''
自己封装的期望条件代码：
解决；一个按钮需要连续按多次才会弹出提示框的场景
自己封装的函数包括：
1、两个输入参数；即点击的目标按钮，弹框内容的捕获
2、通过显示等待的until调用，until中会根据传入的参数实现对这段封装的代码进行多次执行
'''
def muliti_click(target_element, next_element):
    def _inner(driver):
        driver.find_element(*target_element).click()
        # 第一种结果为找到元素，return的内容为 webelement 对象
        # 第二种结果为未找到，driver.find_element(*next_element) 代码报错
        # 但是被 until 中的异常捕获逻辑捕获异常，继续循环，直到最大等待时间到期，超时为止
        return driver.find_element(*next_element)
    return _inner


def wait_until():
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/#/ui_study")
    # 问题：使用官方提供的expected condition无法满足需求
    # 解决方案：自己封装期望条件
    # 期望条件设计：需求 一直点击按钮，直到下一个页面出现为止

    WebDriverWait(driver, 10).until(
        muliti_click(
            (By.ID, "primary_btn"),
            (By.XPATH, "//*[text()='该弹框点击两次后才会弹出']")
        )
    )
    time.sleep(5)

if __name__ == '__main__':
    wait_until()
