# 功能函数
def multiply(a, b):
    return a * b


# =====fixtures========
def setup_module(module):
    print("setup_module================>")


def teardown_module(module):
    print("teardown_module=============>")


def setup_function(function):
    print("setup_function------>")


def teardown_function(function):
    print("teardown_function--->")


def setup():
    print("setup----->")


def teardown():
    print("teardown-->")


# =====测试用例========
def test_multiply_3_4():
    print('test_numbers_3_4')
    assert multiply(3, 4) == 12


def test_multiply_a_3():
    print('test_strings_a_3')
    assert multiply('a', 3) == 'aaa'

