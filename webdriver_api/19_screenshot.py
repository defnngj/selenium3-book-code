"""
* save_screenshot() 截取窗口图片。
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

# 对当前窗口截图，并指定图片的保存位置
driver.save_screenshot("./files/baidu_img.png")
