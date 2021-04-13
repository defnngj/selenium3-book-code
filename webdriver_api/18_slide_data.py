"""
滑动选择日历
"""
from time import sleep
from selenium import webdriver


driver = webdriver.Chrome()

driver.get("http://www.jq22.com/yanshi4976")
driver.set_page_load_timeout(2)
driver.set_script_timeout(2)

sleep(2)
driver.switch_to.frame("iframe")
driver.find_element_by_id("appDate").click()

# 定位要滑动的年、月、日
dwwos = driver.find_elements_by_class_name("dwwo")
year = dwwos[0]
month = dwwos[1]
day = dwwos[2]

# 拨动年
action = webdriver.ActionChains(driver)
action.click_and_hold(year).move_by_offset(0, 100).perform()
action.reset_actions()

# 拨动月
action2 = webdriver.ActionChains(driver)
action2.click_and_hold(month).move_by_offset(0, 150).perform()
action2.reset_actions()

# 拨动天
action3 = webdriver.ActionChains(driver)
action3.click_and_hold(day).move_by_offset(0, 150).perform()
action3.reset_actions()


# 废弃，在新的浏览器和驱动中报错
# action = webdriver.TouchActions(driver)
# action.scroll_from_element(year, 0, 5).perform()
# action.scroll_from_element(month, 0, 30).perform()
# action.scroll_from_element(day, 0, 30).perform()
# ...