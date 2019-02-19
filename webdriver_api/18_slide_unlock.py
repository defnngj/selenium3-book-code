"""
滑动解锁
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException

driver = webdriver.Chrome()
driver.get("https://www.helloweba.com/demo/2017/unlock/")

# 定位滑动块
slider = driver.find_elements_by_class_name("slide-to-unlock-handle")[0]
action = ActionChains(driver)
action.click_and_hold(slider).perform()

for index in range(200):
    try:
        action.move_by_offset(2, 0).perform()
    except UnexpectedAlertPresentException:
        break
    action.reset_actions()
    sleep(0.1)  # 等待停顿时间


# 打印警告框提示
success_text = driver.switch_to.alert.text
print(success_text)
