# 测试模块
# import calc as calc
import logging

import pytest
import yaml

def get_yml_data(level):
    # safe_load: 把yaml格式转成python对象
    # safe_dump: 把python对象 转成yaml格式
    with open("../data.yml", encoding="utf-8") as f:
        result = yaml.safe_load(f)
        add_datas = result.get("add").get(level).get("datas")
        add_ids = result.get("add").get(level).get("ids")
        return [add_datas, add_ids]

class TestCalculator():
    # 定义类变量
    add_P0_datas = get_yml_data("P0")[0]
    add_P0_ids = get_yml_data("P0")[1]
    add_P1_1_datas = get_yml_data("P1_1")[0]
    add_P1_1_ids = get_yml_data("P1_1")[1]
    add_P1_2_datas = get_yml_data("P1_2")[0]
    add_P1_2_ids = get_yml_data("P1_2")[1]
    add_P2_datas = get_yml_data("P2")[0]
    add_P2_ids = get_yml_data("P2")[1]

    # @pytest.mark.p0 为测试用例添加标签
    @pytest.mark.p0
    @pytest.mark.parametrize("x,y,expect", add_P0_datas,ids=add_P0_ids)
    def test_add0(self, x, y, expect,get_calc):
        logging.info(f"参数：{x}, {y},期望结果：{expect}")
        # 测试相加方法
        result = get_calc.add(x, y)
        logging.info(f"结果{result}")
        print(result)
        assert result == expect

    @pytest.mark.p1_1
    @pytest.mark.parametrize('x,y,expect', add_P1_1_datas,ids=add_P1_1_ids)
    def test_add1(self, x, y, expect, get_calc):
        result = get_calc.add(x, y)
        print(result)
        assert result == expect

    @pytest.mark.p1_2
    @pytest.mark.parametrize("x,y,errortype", add_P1_2_datas, ids=add_P1_2_ids)
    def test_add2(self, x, y, errortype, get_calc):
        # 从yaml中获取到的数据是一个字符串，这里需要通过eval将字符串变成一个类型
        with pytest.raises(eval(errortype)) as e:
            result = get_calc.add(x, y)

    # @pytest.mark.run(order=2)  为测试用例添加执行顺序
    @pytest.mark.run(order=2)
    @pytest.mark.p2
    @pytest.mark.parametrize("x,y,errortype", add_P2_datas, ids=add_P2_ids)
    def test_add3(self, x, y, errortype, get_calc):
        # 从yaml中获取到的数据是一个字符串，这里需要通过eval将字符串变成一个类型
        with pytest.raises(eval(errortype)) as e:
            result = get_calc.add(x, y)
