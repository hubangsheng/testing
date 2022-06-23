# __author:lenovo
# date:2022/6/22
import yaml

from utils.log_util import logger


def get_data(filename):
    logger.info("获取数据")
    with open(filename, encoding='UTF-8') as f:
        datas = yaml.safe_load(f)
        return datas