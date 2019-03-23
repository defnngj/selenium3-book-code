"""
原生App测试
"""
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

caps = {}
caps["deviceName"] = "Android Emulator"
caps["automationName"] = "Appium"
caps["platformName"] = "Android"
caps["platformVersion"] = "7.0"
caps["appPackage"] = "com.android.contacts"
caps["appActivity"] = ".activities.PeopleActivity"
caps["noReset"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

# 点击添加按钮
TouchAction(driver).tap(x=942, y=1635).perform()

# 输入联系人信息
driver.find_element_by_android_uiautomator('text("Name")').send_keys("Tom")
driver.find_element_by_android_uiautomator('text("Phone")').send_keys("18611001100");

# 保存联系人
driver.find_element_by_id("com.android.contacts:id/menu_save").click()

driver.quit()

