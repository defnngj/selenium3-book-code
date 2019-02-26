from calculator import Calculator
import unittest


class TestAdd(unittest.TestCase):
    """ add()方法测试 """

    def test_add_integer(self):
        """ 整数相加测试 """
        c = Calculator(3, 5)
        self.assertEqual(c.add(), 8)

    def test_add_decimals(self):
        """ 小数相加测试 """
        c = Calculator(3.2, 5.5)
        self.assertEqual(c.add(), 8)

    def test_add_string(self):
        """ 字符串整数相加测试 """
        c = Calculator("7", "9")
        self.assertEqual(c.add(), 16)

    # ……


class TestSub(unittest.TestCase):
    """ sub()方法测试 """

    def test_sub(self):
        c = Calculator(7, 2)
        result = c.sub()
        self.assertEqual(result, 5)


class TestMul(unittest.TestCase):
    """ mul()方法测试 """

    def test_mul(self):
        c = Calculator(3, 3)
        result = c.mul()
        self.assertEqual(result, 9)


class TestDiv(unittest.TestCase):
    """ div()方法测试 """

    def test_div(self):
        c = Calculator(6, 2)
        result = c.div()
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
