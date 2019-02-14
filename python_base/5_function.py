"""
函数使用
"""


# 定义add()函数
def add(a, b):
    print(a + b)


def add2(a, b):
    return a + b


def add3(a=1, b=2):
    return a + b


# 调用add()函数
add(3, 5)
c = add2(3, 5)
print(c)
c1 = add3()
c2 = add3(3, 5)
print(c1)
print(c2)
