# 测试模块
import pytest
from calculatorTest.pythoncode.calculator import Calculator

class TestCalculator:
    def setup_class(self):
        print("实例化calculator对象")
        # 由于在每个用例中都需要实例化一个对象，所以，可以将实例化对象放在setup_class中，这样每个测试类开始的时候都会执行一遍实例化对象
        self.calc = Calculator()

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    def teardown_class(self):
        print("结束测试")

    @pytest.mark.p0
    @pytest.mark.parametrize("x,y,expect", [[1, 2, 3], [-0.01, 0.02, 0.01], [10, 0.02, 10.02]],
                             ids=["整型", "浮点型", "整型+浮点型"])
    def test_add0(self, x, y, expect):
        # 测试相加方法
        # calc = Calculator()
        result = self.calc.add(x, y)
        print(result)
        assert result == expect

    @pytest.mark.p1
    @pytest.mark.parametrize('x,y,expect', [[98.99, 99, 197.99],
                                            [99, 98.99, 197.99],
                                            [-98.99, -99, -197.99],
                                            [-99, -98.99, -197.99]],
                             ids=["边界值-正1", "边界值-正2", "边界值-负1", "边界值-负2"])
    def test_add1(self, x, y, expect):
        result = self.calc.add(x, y)
        print(result)
        assert result == expect

    @pytest.mark.p1
    @pytest.mark.parametrize("x,y,expect", [[99.01, 0, "参数大小超出范围"]], ids=["无效边界值"])
    def test_add2(self, x, y, expect):
        result = self.calc.add(x, y)
        print(result)
        assert result == expect

    @pytest.mark.p2
    @pytest.mark.parametrize("x,y,errortype", [["文", 9.3, TypeError]], ids=["中文字符"])
    def test_add3(self, x, y, errortype):
        with pytest.raises(errortype) as e:
            result = self.calc.add(x, y)
