"""
* execute_script() 调用JavaScript实现滚动条操作。
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.set_window_size(800, 600)

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)

# 通过javascript设置浏览器窗口的滚动条位置
js = "window.scrollTo(100,450);"
driver.execute_script(js)
sleep(3)

driver.quit()
