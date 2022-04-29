# 测试模块
# import calc as calc
import logging

import allure
import pytest
import yaml


# @pytest.fixture(scope="class")
def get_yml_data(calctpye, level):
    # safe_load: 把yaml格式转成python对象
    # safe_dump: 把python对象 转成yaml格式
    with open("../data.yml", encoding="utf-8") as f:
        result = yaml.safe_load(f)
        add_datas = result.get(calctpye).get(level).get("datas")
        add_ids = result.get(calctpye).get(level).get("ids")
        return [add_datas, add_ids]


# 为测试用例添加分类
# @allure.feature("计算器")  表示大的分类
# @allure.story("相加功能")
@allure.feature("计算器")
class TestCalculator():
    # get_yml_data=get_yaml_data("add")
    # 定义类变量
    add_P0_datas = get_yml_data("add", "P0")[0]
    add_P0_ids = get_yml_data("add", "P0")[1]
    add_P1_1_datas = get_yml_data("add", "P1_1")[0]
    add_P1_1_ids = get_yml_data("add", "P1_1")[1]
    add_P1_2_datas = get_yml_data("add", "P1_2")[0]
    add_P1_2_ids = get_yml_data("add", "P1_2")[1]
    add_P2_datas = get_yml_data("add", "P2")[0]
    add_P2_ids = get_yml_data("add", "P2")[1]
    div_P0_datas = get_yml_data("div", "P0")[0]
    div_P0_ids = get_yml_data("div", "P0")[1]
    div_P1_datas = get_yml_data("div", "P1")[0]
    div_P1_ids = get_yml_data("div", "P1")[1]
    div_P2_datas = get_yml_data("div", "P2")[0]
    div_P2_ids = get_yml_data("div", "P2")[1]

    # @pytest.mark.p0 为测试用例添加标签
    @allure.story("相加功能--有步骤")
    @allure.title("P0级别加法运算")
    @pytest.mark.P0
    @pytest.mark.parametrize("x,y,expect", add_P0_datas, ids=add_P0_ids)
    def test_add0(self, x, y, expect, get_calc):
        logging.info(f"参数：{x}, {y},期望结果：{expect}")
        # 测试相加方法
        with allure.step("相加操作"):
            result = get_calc.add(x, y)
        logging.info(f"结果{result}")
        print(result)
        with allure.step("结果验证"):
            assert result == expect

    @allure.story("相加功能")
    @allure.title("P1_1级别加法运算")
    @pytest.mark.P1_1
    @pytest.mark.parametrize('x,y,expect', add_P1_1_datas, ids=add_P1_1_ids)
    def test_add1(self, x, y, expect, get_calc):
        result = get_calc.add(x, y)
        allure.attach.file("./image/logo.jpeg", name="截图", attachment_type=allure.attachment_type.JPG,
                           extension=".JPEG")
        print(result)
        assert result == expect

    @allure.story("相加功能")
    @allure.title("P1_2级别加法运算")
    @pytest.mark.P1_2
    @pytest.mark.parametrize("x,y,errortype", add_P1_2_datas, ids=add_P1_2_ids)
    def test_add2(self, x, y, errortype, get_calc):
        # 从yaml中获取到的数据是一个字符串，这里需要通过eval将字符串变成一个类型
        with pytest.raises(eval(errortype)) as e:
            result = get_calc.add(x, y)

    # @pytest.mark.run(order=2)  为测试用例添加执行顺序
    @pytest.mark.run(order=2)
    @allure.title("P2级别加法运算")
    @pytest.mark.P2
    @pytest.mark.parametrize("x,y,errortype", add_P2_datas, ids=add_P2_ids)
    def test_add3(self, x, y, errortype, get_calc):
        # 从yaml中获取到的数据是一个字符串，这里需要通过eval将字符串变成一个类型
        with pytest.raises(eval(errortype)) as e:
            result = get_calc.add(x, y)

    @allure.story("除法")
    @allure.title("P0级别除法运算")
    @pytest.mark.P0
    @pytest.mark.parametrize('x,y,expect', div_P0_datas, ids=div_P0_ids)
    def test_div0(self, x, y, expect, get_calc):
        logging.info(f"参数：{x},{y},期望结果：{expect}")
        if expect == "ZeroDivisionError":
            with pytest.raises(eval(expect)) as e:
                # 添加操作步骤
                with allure.step("除数为0的异常情况"):
                    result = get_calc.div(x, y)
                    logging.info(f"结果：{result}")
        else:
            with allure.step("除法运算"):
                result = get_calc.div(x, y)
            with allure.step("验证运算结果"):
                assert result == expect

    @allure.story("除法运算异常情况case")
    @allure.title("P1级别除法运算")
    @pytest.mark.P1
    @pytest.mark.parametrize('x,y,expect', div_P1_datas, ids=div_P1_ids)
    def test_div1(self, x, y, expect, get_calc):
        logging.info(f"参数：{x},{y}，期望结果：{expect}")
        if expect =="TypeError":
            with pytest.raises(eval(expect)) as e:
                with allure.step("除数或被除数为中英文字符的情况"):
                    result = get_calc.div(x, y)
                    logging.info(f"验证测试结果：{result}")
                    # assert result == expect
        # elif expect == "SyntaxError":
        #     with pytest.raises(eval(expect)) as e:
        #         with allure.step("除数或被除数为特殊字符的情况"):
        #             result = get_calc.div(x, y)
        #             logging.info(f"验证测试结果：{result}")

    @allure.story("除法运算除数或被除数不存在的情况")
    @allure.title("P2级别除法运算，除数或被除数不存在")
    @pytest.mark.P2
    @pytest.mark.parametrize('x,y,expect', div_P2_datas, ids=div_P2_ids)
    def test_div2(self, x, y, expect, get_calc):
        logging.info(f"参数：{x},{y}，期望结果：{expect}")
        if expect == "TypeError":
            with pytest.raises(eval(expect)) as e:
                with allure.step("除数或被除数为空或不存在的情况"):
                    result = get_calc.div(x, y)
                    logging.info(f"验证测试结果：{result}")
                    # assert result == expect
