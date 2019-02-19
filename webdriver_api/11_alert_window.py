"""
* text：返回 alert/confirm/prompt 中的文字信息。
* accept()：接受现有警告框。
* dismiss()：解散现有警告框。
* send_keys(keysToSend)： 发送文本至警告框。
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# 打开搜索设置
link = driver.find_element_by_link_text('设置').click()
driver.find_element_by_link_text("搜索设置").click()
sleep(2)

# 保存设置
driver.find_element_by_class_name("prefpanelgo").click()

# 获得警告框
alert = driver.switch_to.alert

# 获得警告框提示信息
alert_text = alert.text
print(alert_text)

# 接受警告框
alert.accept()

driver.quit()
