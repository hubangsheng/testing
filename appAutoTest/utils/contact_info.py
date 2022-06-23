from faker import Faker

# pip install Faker
# Mock 假数据
from appAutoTest.utils.log_util import logger


class ContactInfo:
    # 定义类方法
    @classmethod
    def get_name(cls):
        name = Faker('zh_CN').name()
        logger.info(f"name: {name}")
        return name

    @classmethod
    def get_phonenum(cls):
        phonenum = Faker('zh_CN').phone_number()
        logger.info(f"phonenum: {phonenum}")
        return phonenum


# if __name__ == '__main__':
#     ContactInfo.get_name()
#     ContactInfo.get_phonenum()