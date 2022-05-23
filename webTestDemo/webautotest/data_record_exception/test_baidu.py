import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

'''
目标1、实现代码异常的时候，截图/打印page_source
实现方法：try catch 配合截图/ page_source操作

问题一、异常处理会影响用例本身的结果
解决方案：在exception 之后再把异常抛出

问题二、异常捕获处理代码和实际的业务无关，不能耦合
解决方案：使用装饰器装饰用例或者相关方法，就不会体现在源码中了，（注意：一定要先学习装饰器）
    1、先把装饰器的架子搭好
    2、把相关的逻辑嵌套进来
'''


def ui_exception_record(func):
    def inner(*args, **kwargs):
        # 获取被装饰方法的self 也就是实例对象
        # 通过self就可以拿到声明的实例变量driver
        # 前提条件：1、被装饰的方法是一个实例方法， 2、实例需要有实例变量self.driver

        # 问题：需要通过driver实例截图/打印 page_source，装饰器需要先去获取driver对象：
        # 两种方案，
        # 方案一、将driver = args[0].driver放在try...except...的except代码块中
        # 方案二、将driver的实例对象放在setup_class函数中，在用例一开始的时候就创建这个实例
        driver = args[0].driver
        try:
            # 当被装饰的方法/函数发生异常就捕获并做数据记录
            return func(*args, **kwargs)
        except Exception:
            timestamp = int(time.time())
            # 注意：需要提前创建好images 目录
            image_path = f"./images/image_{timestamp}.PNG"
            page_source_path = f"./page_source/page_source_{timestamp}.html"
            # 截图
            driver.save_screenshot(image_path)
            # 记录page_source
            with open(page_source_path, "w", encoding="u8") as f:
                f.write(driver.page_source)

            # 将截图放到报告的数据中
            allure.attach.file(image_path, name="pagesource",
                               attachment_type=allure.attachment_type.PNG)
            # 将pagesource 记录到报告中
            # 如果想要 html 源码格式使用text，如果想要页面格式使用html
            allure.attach.file(page_source_path, name="pagesource",
                               attachment_type=allure.attachment_type.HTML)
            raise Exception
    return inner


class TestBaidu:
    def setup_class(self):
        self.driver = webdriver.Chrome()

    def teardown_class(self):
        self.driver.quit()

    @ui_exception_record
    def findui(self):
        # print(res)
        return self.driver.find_element(By.ID, "su")


    def test_baidu(self):
        self.driver.get("https://www.baidu.com/")
        # print(self.findui)
        self.findui().click()

