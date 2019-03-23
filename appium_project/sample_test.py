from appium import webdriver


caps = {
    "deviceName": " MEIZU_E3",
    "automationName": "Appium",
    "platformName": "Android",
    "platformVersion": "7.1.1",
    "appPackage": " com.meizu.flyme.flymebbs",
    "appActivity": ".ui.LoadingActivity",
    "noReset": True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)

# 论坛贴子搜索
search_box = driver.find_element_by_id("com.meizu.flyme.flymebbs:id/r9")
search_box.click()
search_box.send_keys(u"魅族16")
driver.find_element_by_id("com.meizu.flyme.flymebbs:id/rc").click()

driver.quit()

