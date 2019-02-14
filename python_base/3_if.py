"""
if语句的用法
"""

a = 2
b = 3
if a > b:
    print("a max!")
else:
    print("b max!")


if 2+2 == 4:
    print("true")
else:
    print("false")


s = "hello"
ss = "hello world"
if s in ss:
    print("Contain")
else:
    print("Not Contain")


if True:
    print("true")
else:
    print("false")


# 成绩
result = 72
if result >= 90:
    print('优秀')
elif result >= 70:
    print('良好')
elif result >= 60:
    print('及格')
else:
    print('不及格')