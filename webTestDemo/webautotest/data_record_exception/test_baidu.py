import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBaidu:
    def test_baidu(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        try:
            self.driver.find_element(By.ID, "su")
        except Exception:
            timestamp = int(time.time())
            image_path = f"./images/image_{timestamp}.PNG"
            page_source_path = f"./page_source/page_source_{timestamp}.html"
            self.driver.save_screenshot(image_path)
            with open(page_source_path, "w", encoding="u8") as f:
                f.write(self.driver.page_source)

            # 将截图放到报告的数据中
            allure.attach.file(image_path, name="pagesource", attachment_type=allure.attachment_type.PNG)
            # 将pagesource 记录到报告中
            # 如果想要 html 源码格式使用text，如果想要页面格式使用html
            allure.attach.file(page_source_path, name="pagesource", attachment_type=allure.attachment_type.HTML)
            raise Exception