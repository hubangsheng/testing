# __author:lenovo
# date:2022/6/16
from appium import webdriver

from base.base_page import BasePage
from page.main_page import MainPage
from utils.log_util import logger


class App(BasePage):
    def start(self):
        # 启动
        # 资源初始化
        # 打开【企业微信】应用
        if self.driver == None:
            caps = {}
            caps["platformName"] = "Android"
            # mac: adb logcat ActivityManager:I | grep "cmp"
            # windows:adb logcat ActivityManager:I | findstr "cmp"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            # adb devices
            caps["deviceName"] = "49a66be1"
            # "True" 是绝对不可以的  要么是"true" 要么是 True
            # 防止清缓存
            caps["noReset"] = "true"
            # 尽量不要在真实的测试环境下使用
            # caps["dontStopAppOnReset"] = "true"
            # 动态页面等待0秒 再去查找元素， 默认是等待10秒
            caps["settings[waitForIdleTimeout]"] = 0
            # 创建driver ,与appium server建立连接，返回一个 session
            # driver 变成self.driver 由局部变量变成实例变量，就可以在其它的方法中引用这个实例变量了
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            # 隐式等待是全局的等待方式
            self.set_implicitly(self.implicitly_wait_time)
        else:
            logger.info("driver 已存在，复用已有的driver")
            # 会自动的启动desire caps里面记录的页面
            self.driver.launch_app()
            # 启动另外一个app的页面
            # self.driver.start_activity()

        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def quit(self):
        self.driver.quit()

    def goto_main(self):
        # 进入到首页入口
        return MainPage(self.driver)
