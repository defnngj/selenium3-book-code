# 导入time模块
import time
print(time.ctime())

# 直接导入ctime()方法
from time import ctime
print(ctime())


# 直接导入模块下的多个方法
from time import time, sleep


# 导入time模块下的所有方法
from time import *

print(ctime())
print("休眠两秒")
sleep(2)
print(ctime())


# 对导入的sleep模块重命名
from time import sleep as sys_sleep


def sleep(sec):
    print("this is I defined sleep() ")


print(sleep(1))


import time

help(time)
