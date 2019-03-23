"""
移动Web测试
"""
from appium import webdriver

caps = {}
caps["deviceName"] = "Android Emulator"
caps["automationName"] = "Appium"
caps["platformName"] = "Android"
caps["platformVersion"] = "7.0"
caps["browserName"] = "Chrome"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

driver.get("https://m.baidu.com")

driver.find_element_by_id("index-kw").send_keys("appium mobile web")
driver.find_element_by_id("index-bn").click()

driver.quit()
