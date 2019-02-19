"""
* get_cookies() 获得所有 cookie 信息。
* get_cookie(name) 返回字典的 key 为“ name”的 cookie 信息。
* add_cookie(cookie_dict) 添加 cookie。“ cookie_dict”指字典对象，必须有name和value 值。
* delete_cookie(name,optionsString)  删除 cookie 信息。“name”是要删除的 cookie 的名称，
                                   “optionsString”是该 cookie 的选项，目前支持的选项包括“路径”，“域”。
* delete_all_cookies() 删除所有 cookie 信息。
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 获得所有cookie信息并打印
cookie = driver.get_cookies()
print(cookie)

# 添加cookie信息
driver.add_cookie({'name': 'key-aaaaaaa', 'value': 'value-bbbbbb'})

# 遍历指定的cookies
for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'], cookie['value']))

driver.quit()
