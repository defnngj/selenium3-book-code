"""
类、方法的使用
"""


# 定义MyClass类
class MyClass(object):

    def say_hello(self, name):
        return "hello, " + name


# 调用MyClass类
mc = MyClass()
print(mc.say_hello("tom"))


class A:

    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b


# B类继承A类
class B(A):
    
    def sub(self, a, b):
        return a - b


# 调用类时需要传入初始化参数
count = A('4', 5)
print(count.add())

print(B(2, 3).add())
