"""
混合App测试
"""
from appium import webdriver
from time import sleep


caps = {}
caps["deviceName"] = "Android Emulator"
caps["automationName"] = "Appium"
caps["platformName"] = "Android"
caps["platformVersion"] = "7.0"
caps["appPackage"] = "com.example.anwebview"
caps["appActivity"] = ".MainActivity"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

# 获得当前上下文
context = driver.context
print(context)

# 获得所有上下文
all_context = driver.contexts
for context in all_context:
    print(context)

# 切换上下文
driver.switch_to.context("WEBVIEW_com.example.anwebview")

# 进入webview模式进行操作
driver.find_element_by_id("index-kw").send_keys("appium webView")
driver.find_element_by_id("index-bn").click()
sleep(2)

driver.quit()



