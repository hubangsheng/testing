"""类目列表页"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from po_test_demo.page_objects.base_page import BasePage
from po_test_demo.utils.log_utils import logger


class CategoryListPage(BasePage):
    """类目列表页：点击添加"""
    __BTN_ADD = (By.XPATH, "//*[text()='添加']")
    __MSG_ADD_OPERATE = (By.XPATH, '//p[contains(text(),"创建")]')
    __MSG_DEL_OPERATE = (By.XPATH, '//p[contains(text(),"删除")]')

    def click_add(self):
        logger.info("类目列表页：点击添加")
        # 点击”添加“按钮
        self.do_find(self.__BTN_ADD).click()

        # ==> 创建类目页面

        from po_test_demo.page_objects.category_create_page import CategoryCreatePage
        return CategoryCreatePage(self.driver)

    """类目列表页：获取操作结果"""

    def get_operate_result(self):
        logger.info("类目列表页：获取添加操作结果")
        # 获取冒泡消息文本
        # element = WebDriverWait(self.driver, 10).\
        #     until(expected_conditions.visibility_of_element_located()
        element = self.wait_element_until_visible(self.__MSG_ADD_OPERATE)
        msg = element.text
        logger.info(f'冒泡信息为:{msg}')
        # ==> 返回消息文本
        return msg

    def delete_category(self, category_name):
        # 删除指定商品
        logger.info(f"删除指定商品:{category_name}")
        self.do_find(By.XPATH, f"//*[text()='{category_name}']/../..//*[text()='删除']").click()
        return CategoryListPage(self.driver)

    # 同一个功能，返回结果不一样，根据PO设计原则，需要将这两部分分开写
    def get_delete_result(self):
        logger.info("类目列表页：获取删除商品操作结果")
        # 获取删除时的冒泡消息文本
        element = self.wait_element_until_visible(self.__MSG_DEL_OPERATE)
        msg = element.text
        logger.info(f'冒泡信息为:{msg}')
        # ==> 返回消息文本
        return msg
