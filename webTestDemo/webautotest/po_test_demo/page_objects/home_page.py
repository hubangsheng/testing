"""首页"""
from selenium.webdriver.common.by import By

from po_test_demo.page_objects.base_page import BasePage
from po_test_demo.utils.log_utils import logger

class HomePage(BasePage):
    __MENU_MALL_MANAGE = (By.XPATH, "//*[text()='商场管理']")
    __MENU_PRODUCT_CATEGORY = (By.XPATH, "//*[text()='商品类目']")
    """系统首页：进入商品类目"""

    def go_to_category(self):
        logger.info("系统首页：进入商品类目")
        logger.info("进入商品类目")
        # 点击菜单”商场管理“
        # 点击菜单”商品类目“
        self.do_find(self.__MENU_MALL_MANAGE).click()
        self.do_find(self.__MENU_PRODUCT_CATEGORY).click()

        # ==> 类目列表页面
        from po_test_demo.page_objects.category_list_page import CategoryListPage
        return CategoryListPage(self.driver)