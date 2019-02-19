"""
* Select  操作select标签的下拉框。
* select_by_value()  选择value属性选择。
* select_by_visible_text() 通过选项名称选择。
* select_by_index() 通过索引选择
"""
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# 打开搜索设置
link = driver.find_element_by_link_text('设置').click()
driver.find_element_by_link_text("搜索设置").click()
sleep(2)

# 搜索结果显示条数
sel = driver.find_element_by_xpath("//select[@id='nr']")

# value="20"
Select(sel).select_by_value('20')
sleep(2)

# <option>每页显示50条</option>
Select(sel).select_by_visible_text("每页显示50条")
sleep(2)

# 根据选项的索引选择
Select(sel).select_by_index(0)
sleep(2)

driver.quit()
