"""
126邮箱登录/退出
"""
from time import sleep
from selenium import webdriver
from module import Mail

driver = webdriver.Chrome()
driver.get("http://www.126.com")

user_info = [
    {"username": "", "password": ""},
    {"username": "", "password": "123"},
    {"username": "user", "password": ""},
    {"username": "error", "password": "error"},
    {"username": "admin", "password": "admin123"},
]

# 调用Mail类
mail = Mail(driver)

# 登录账号为空
mail.login(user_info[0]["username"], user_info[0]["password"])

# 用户名为空
mail.login(user_info[1]["username"], user_info[1]["password"])

# 密码为空
mail.login(user_info[2]["username"], user_info[2]["password"])

# 用户名密码错误
mail.login(user_info[3]["username"], user_info[3]["password"])

# 管理员登录
mail.login(user_info[4]["username"], user_info[4]["password"])

# ……
