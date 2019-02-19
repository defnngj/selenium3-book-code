"""
*  set_window_size()   设置浏览器宽、高
*  maximize_window()   设置浏览器全屏
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://m.baidu.com")

# 参数数字为像素点
print("设置浏览器宽480、高800显示")
driver.set_window_size(480, 800)

# 设置浏览器全屏
driver.maximize_window()

driver.quit()
