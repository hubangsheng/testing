# __author:lenovo
# date:2022/7/15
import json

import pytest
import requests

from utils.log_util import logger


class TestLitemall:
    def setup_class(self):
        # 获取管理端的 token
        admin_url = "http://litemall.hogwarts.ceshiren.com/admin/auth/login"
        admin_data = {"username": "admin123", "password": "admin123", "code": ""}
        r = requests.post(admin_url, json=admin_data)
        # print(r.json()["data"]["token"])
        self.admin_token = r.json()["data"]["token"]

        # 获取客户端的 token
        client_url = "http://litemall.hogwarts.ceshiren.com/wx/auth/login"
        client_data = {"username": "user123", "password": "user123"}
        u_r = requests.post(client_url, json=client_data)
        self.client_token = u_r.json()['data']['token']

    # 清除测试数据
    # 调用删除接口，直接通过删除商品接口进行清理
    def teardown(self):
        del_url = "http://litemall.hogwarts.ceshiren.com/admin/goods/delete"
        r = requests.post(del_url, json={"id":self.goods_id}, headers={"X-Litemall-Admin-Token": self.admin_token})
        print(r.json())
        logger.info(f"删除的商品信息为{json.dumps(r.json(), indent=2, ensure_ascii=False)}")

    # 问题：没有执行test_get_admin_token这个方法，所以self.token 就不会被声明就会报错”'TestLitemall' object has no attribute 'token'”
    # 解决，self.token 的声明一定要在test_add_goods方法执行之前完成，可以使用setup_class完成提前变量的声明

    # 上架商品接口测试
    @pytest.mark.parametrize('goods_name', ['AD钙奶1', 'AD钙奶2'])
    def test_add_goods(self, goods_name):
        # 上架不同的商品
        url = "http://litemall.hogwarts.ceshiren.com/admin/goods/create"
        goods_data = {
            "goods": {"picUrl": "", "gallery": [], "isHot": False, "isNew": True, "isOnSale": True, "goodsSn": "9002",
                      "name": goods_name}, "specifications": [{"specification": "规格", "value": "标准", "picUrl": ""}],
            "products": [{"id": 0, "specifications": ["标准"], "price": "100", "number": "66", "url": ""}],
            "attributes": []}

        # 问题：token 是手动复制进去的，一旦发生变化，还需要再次修改
        # 解决方案：token 需要自动完成获取，并且赋值
        r = requests.post(url, json=goods_data,
                          headers={"X-Litemall-Admin-Token": self.admin_token})
        # print(r.json())
        logger.info(f"上架商品接口的相应信息为{json.dumps(r.json(), indent=2, ensure_ascii=False)}")

        # 获取商品的 goodsId
        goods_list_url = "http://litemall.hogwarts.ceshiren.com/admin/goods/list"
        goods_list_data = {
            "name": goods_name,
            "order": "desc",
            "sort": "add_time"
        }
        c_r = requests.get(goods_list_url, params=goods_list_data,
                           headers={"X-Litemall-Admin-Token": self.admin_token})
        self.goods_id = c_r.json()['data']['list'][0]['id']
        logger.debug(f"商品goodsId为{json.dumps(c_r.json(), indent=2, ensure_ascii=False)}")

        # 获取商品的 productId
        goods_detail_url = "http://litemall.hogwarts.ceshiren.com/admin/goods/detail"
        d_r = requests.get(goods_detail_url, params={"id": self.goods_id},
                           headers={"X-Litemall-Admin-Token": self.admin_token})
        # print()
        self.product_id = d_r.json()['data']['products'][0]['id']
        logger.debug(f"商品product_id为{json.dumps(d_r.json(), indent=2, ensure_ascii=False)}")

        # 添加商品到购物车，客户端
        url = "http://litemall.hogwarts.ceshiren.com/wx/cart/add"

        # 问题：goosId和productId是写死的，变量的传递没有完成
        # 解决方案：goosId和productId从其他接口获取
        cart_data = {"goodsId": self.goods_id, "number": 1, "productId": self.product_id}
        r = requests.post(url, json=cart_data, headers={"X-Litemall-Token": self.client_token})
        # print(r.json())
        logger.info(f"购物车商品信息{json.dumps(r.json(), indent=2, ensure_ascii=False)}")


