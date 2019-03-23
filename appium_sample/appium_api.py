"""
appium API
"""
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

caps = dict()
caps["deviceName"] = "Android Emulator"
caps["automationName"] = "Appium"
caps["platformName"] = "Android"
caps["platformVersion"] = "7.0"
caps["appPackage"] = "com.android.calculator2"
caps["appActivity"] = ".Calculator"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

# 安装app
driver.install_app("D:\\android\\apk\\ContactManager.apk")

# 删除app
driver.remove_app('com.example.android.apis')

# 关闭app
driver.close_app()

# 重启app
driver.launch_app()

# 判断app是否安装
result = driver.is_app_installed('com.example.android.apis')
print(result)

#  将APP置于后台
driver.background_app(5)

# 重置应用
driver.reset()

# 输入字符串
driver.find_element_by_name("Name").send_keys("Jack")

# 模拟按键
# 键入数字“186“
driver.keyevent(1)   # 1
driver.keyevent(15)  # 8
driver.keyevent(13)  # 6

# 键入字符串“HELLO“
driver.keyevent(36)  # H
driver.keyevent(33)  # E
driver.keyevent(40)  # L
driver.keyevent(40)  # L
driver.keyevent(43)  # O


# 定位要按压的元素
el = driver.find_element_by_android_uiautomator('text("Name")')
# 对某个元素执行按压操作
TouchAction(driver).press(el).release().perform()
# 堆屏幕某个位置（x,y坐标）执行按压操作
TouchAction(driver).press(x=0, y=308).release().perform()

# 执行点击控件
TouchAction(driver).tap(el).perform()
TouchAction(driver).tap(x=0, y=308).perform()
TouchAction(driver).tap(el, count=2).perform()

# 执行长按压操作
el = driver.find_element_by_android_uiautomator('text("Name")')
TouchAction(driver).long_press(el).perform()
TouchAction(driver).long_press(x=0, y=308).perform()
TouchAction(driver).long_press(el, duration=2000).perform()

# 暂停
TouchAction(driver).wait(1000).perform()
TouchAction(driver).wait(5000).perform()

# 执行动作链
els = driver.find_elements_by_class_name('listView')
a1 = TouchAction()
a1.press(els[0])\
    .move_to(x=10, y=0)\
    .move_to(x=10, y=-75)\
    .move_to(x=10, y=-600)\
    .release()

a2 = TouchAction()
a2.press(els[1]) \
    .move_to(x=10, y=10)\
    .move_to(x=10, y=-300)\
    .move_to(x=10, y=-600)\
    .release()

ma = MultiAction(driver, els[0])
ma.add(a1, a2)
ma.perform()

driver.lock(seconds=3)  # 熄屏3秒


# 获取当前APP包名
package = driver.current_package
print(package)

# 得到当前APP的activity
activity = driver.current_activity
print(activity)

# 收起虚拟键盘
driver.hide_keyboard()

# 获得屏幕分辨率
windows = driver.get_window_size()
print(windows["width"])
print(windows["height"])

# 拉取文件
driver.pull_file('Library/AddressBook/AddressBook.sqlitedb')


# 推送文件
data = "some data for the file"
path = "/data/local/tmp/file.txt"
driver.push_file(path, data.encode('base64'))

driver.quit()
