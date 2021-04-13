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
driver.get('https://www.w3school.com.cn/tiy/t.asp?f=eg_html_select')
driver.set_page_load_timeout(2)
driver.set_script_timeout(2)

# 切换表单
driver.switch_to.frame("iframeResult")

# 定位select标签
sel = driver.find_element_by_tag_name("select")

# value="saab"
Select(sel).select_by_value('saab')
sleep(2)

# <option>Opel</option>
Select(sel).select_by_visible_text("Opel")
sleep(2)

# 根据选项的索引选择
Select(sel).select_by_index(3)
sleep(2)

driver.quit()
