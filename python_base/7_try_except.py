try:
    open("abc.txt", 'r')
except FileNotFoundError:
    print("异常了!")

try:
    print(a)
except FileNotFoundError:
    print("异常了!")

try:
    open("abc.txt", 'r')
    print(a)
except BaseException:
    print("异常了!")

try:
    open("abc.txt", 'r')
    print(a)
except BaseException as msg:
    print(msg)


try:
    a = "异常测试："
    print(a)
except NameError as msg:
    print(msg)
else:
    print("没有异常时执行!")


try:
    print(a)
except NameError as msg:
    print(msg)
finally:
    print("不管是否异常，都会被执行。")


# 定义say_hello()函数
def say_hello(name=None):
    if name is None:
        raise NameError('"name" cannot be empty')
    else:
        print("hello, %s" %name)


# 调用say_hello()函数
say_hello()
