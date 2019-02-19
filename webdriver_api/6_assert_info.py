"""
*  title         获取当前页面title
*  current_url   获取当前页面URL
*  text          获得文本信息
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
print('Before search================')

# 打印当前页面title
title = driver.title
print("title:"+ title)

# 打印当前页面URL
now_url = driver.current_url
print("URL:"+now_url)

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)

print('After search================')

# 再次打印当前页面title
title = driver.title
print("title:"+title)

# 打印当前页面URL
now_url = driver.current_url
print("URL:"+now_url)

# 获取搜索结果条数
num = driver.find_element_by_class_name('nums').text
print("result:"+num)

driver.quit()
