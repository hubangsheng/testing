"""创建类目页面"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from po_test_demo.page_objects.base_page import BasePage
from po_test_demo.utils.log_utils import logger
from po_test_demo.utils.web_util import click_exception


class CategoryCreatePage(BasePage):

    __INPUT_CATEGORY_NAME = (By.CSS_SELECTOR, ".el-input__inner")
    __BTN_CONFIRM = (By.CSS_SELECTOR, ".dialog-footer .el-button--primary")

    """创建类目页面：创建类目"""
    def create_category(self, category_name):
        logger.info(f"创建类目页面：创建{category_name}类目")
        # 输入“类目名称”
        self.do_send_keys(category_name, self.__INPUT_CATEGORY_NAME)
        # 点击“确定”按钮
        WebDriverWait(self.driver, 10).until(click_exception(*self.__BTN_CONFIRM))
        # ==> 类目列表页面
        from po_test_demo.page_objects.category_list_page import CategoryListPage
        return CategoryListPage(self.driver)