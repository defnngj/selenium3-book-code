# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

caps = {}
caps["deviceName"] = "Android Emulator"
caps["automationName"] = "Appium"
caps["platformName"] = "Android"
caps["platformVersion"] = "7.0"
caps["appPackage"] = "com.android.calculator2"
caps["appActivity"] = ".Calculator"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

TouchAction(driver).tap(x=154, y=1342).perform()
TouchAction(driver).tap(x=889, y=1603).perform()
TouchAction(driver).tap(x=386, y=1346).perform()
TouchAction(driver).tap(x=623, y=1587).perform()

driver.quit()