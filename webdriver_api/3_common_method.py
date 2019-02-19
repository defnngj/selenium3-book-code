"""
*  clear()：				清除文本。
*  send_keys(*value)：	模拟按键输入。
*  click()：				单击元素。
*  size     返回元素的尺寸。
*  text     获取元素的文本。
*  get_attribute(name)   获得属性值。
*  is_displayed()        设置该元素是否用户可见。
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

# submit 提交表单
search_text = driver.find_element_by_id('kw')
search_text.send_keys('selenium')
seearch.submit()

# 获得输入框的尺寸
size = driver.find_element_by_id('kw').size
print(size)

# 返回百度页面底部备案信息
text = driver.find_element_by_id("cp").text
print(text)

# 返回元素的属性值，可以是 id、 name、 type 或其他任意属性
attribute = driver.find_element_by_id("kw").get_attribute('type')
print(attribute)

# 返回元素的结果是否可见，返回结果为 True 或 False
result = driver.find_element_by_id("kw").is_displayed()
print(result)

driver.quit()
