"""
* send_keys(Keys.BACK_SPACE) 删除键（BackSpace）
* send_keys(Keys.SPACE) 空格键(Space)
* send_keys(Keys.TAB) 制表键(Tab)
* send_keys(Keys.ESCAPE) 回退键（Esc）
* send_keys(Keys.ENTER) 回车键（Enter）
* send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）
* send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）
* send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）
* send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V）
* send_keys(Keys.F1) 键盘 F1
  ……
* send_keys(Keys.F12) 键盘 F12
"""
from selenium import webdriver
# 引入Keys模块
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 输入框输入内容
driver.find_element_by_id("kw").send_keys("seleniumm")

# 删除多输入的一个m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

# 输入空格键+“教程”
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys("教程")

# ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')

# ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')

# ctrl+v 粘贴内容到输入框
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')

# 通过回车键来代替单击操作
driver.find_element_by_id("su").send_keys(Keys.ENTER)

driver.quit()
