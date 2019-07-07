"""
使用appium AI定位方法
"""
from appium import webdriver
from time import sleep


CAPS = {
    "deviceName": " MEIZU_E3",
    "automationName": "Appium",
    "platformName": "Android",
    "platformVersion": "7.1.1",
    "appPackage": " com.meizu.flyme.flymebbs",
    "appActivity": ".ui.LoadingActivity",
    "noReset": True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "customFindModules": {"ai": "test-ai-classifier"},
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', CAPS)
sleep(3)

driver.find_element_by_custom("ai:search").click()
driver.find_element_by_id("ai:search").send_keys("flyme")
driver.find_element_by_id("com.meizu.flyme.flymebbs:id/o7").click()
result = driver.find_elements_by_id("com.meizu.flyme.flymebbs:id/a2a")[0].text
print(result)

driver.quit()
