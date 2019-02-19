"""
滑动选择日历
"""
from time import sleep
from selenium import webdriver


driver = webdriver.Chrome()

driver.get("http://www.jq22.com/yanshi4976")
sleep(2)
driver.switch_to.frame("iframe")
driver.find_element_by_id("appDate").click()

# 定位要滑动的年、月、日
dwwos = driver.find_elements_by_class_name("dwwo")
year = dwwos[0]
month = dwwos[1]
day = dwwos[2]

action = webdriver.TouchActions(driver)
action.scroll_from_element(year, 0, 5).perform()
action.scroll_from_element(month, 0, 30).perform()
action.scroll_from_element(day, 0, 30).perform()
# ……