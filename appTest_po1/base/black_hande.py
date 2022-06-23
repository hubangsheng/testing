# __author:lenovo
# date:2022/6/21
import os

import allure
from appium.webdriver.common.appiumby import AppiumBy


# black_list 存放点掉异常弹窗的元素，如：关闭按钮，确定按钮，取消按钮....
black_list = [(AppiumBy.XPATH, "//*[@text='确定']")]


def black_wrapper(fun):
    """
    定义一个装饰器，作用是处理用例运行期间的所有异常弹窗
    :param fun:
    :return:
    """

    def run(*args, **kwargs):
        from base.base_page import BasePage
        basepage: BasePage = args[0]
        try:
            return fun(*args, **kwargs)
        except Exception as e:
            curtime = basepage.get_time()
            # 将当前时间按指定的格式拼接到文件名上
            tmp_name = curtime + '.png'
            # 存储路径拼接  os.path.dirname(__file__) 获取当前文件所在路径；
            # .. 表示当前路径上一级路径；
            # images 表示需要存储的文件夹名称
            # tmp_name 表示存储的截图文件名称
            tmp_path = os.path.join(os.path.dirname(__file__), "..", "images", tmp_name)
            # 添加截图功能
            basepage.screenshot(tmp_path)
            # 将截图通过 allure 添加到测试报告中
            allure.attach.file(tmp_path, name="截图", attachment_type=allure.attachment_type.PNG)
            for black in black_list:
                ales = basepage.driver.find_elements(*black)
                if len(ales) > 0:
                    ales[0].click()
                    return fun(*args, **kwargs)
            raise e

    return run
