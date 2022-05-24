from po_test_demo.utils.log_utils import logger

# 显示等待，自定义显示等待条件
def click_exception(by, element, max_attempts=5):
    def _inner(driver):
        actul_attempts = 0  # 实际点击次数
        while actul_attempts < max_attempts:
            actul_attempts += 1  # 每次循环，实际点击次数加1
            try:
                driver.find_element(by, element).click()
                return True
            except Exception:
                logger.debug("点击的时候出现了一次异常")
            # 当实际点击次数大雨最大点击次数时，结束循环并抛出异常
        raise Exception("超出了最大点击次数")

    return _inner