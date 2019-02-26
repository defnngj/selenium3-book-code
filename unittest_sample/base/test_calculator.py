from calculator import Calculator


def test_add():
    c = Calculator(3, 5)
    result = c.add()
    assert result == 8, '加法运算失败!'

def test_sub():
    c = Calculator(7, 2)
    result = c.sub()
    assert result == 5, '减法运算失败!'

def test_mul():
    c = Calculator(3, 3)
    result = c.mul()
    assert result == 10, '乘法运算失败!'

def test_div():
    c = Calculator(6, 2)
    result = c.div()
    assert result == 3, '除法运算失败!'


if __name__ == '__main__':
    test_add()
    test_sub()
    test_mul()
    test_div()
