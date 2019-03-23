# from selenium import webdriver
#
# # 引用Chrome浏览器配置
# desired_caps = {
#     "browserName": "chrome",
#     "version": "",
#     "platform": "ANY",
# }
# driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
#                 desired_capabilities=desired_caps)


from appium import webdriver

# 定义Android运行环境
desired_caps = {
    'deviceName': 'Android Emulator',
    'automationName': 'Appium',
    'platformName': 'Android',
    'platformVersion': '7.0',
    'appPackage': 'com.android.calculator2',
    'appActivity': '.Calculator',
}
driver = webdriver.Remote(command_executor='http://localhost:4723/wd/hub',
                          desired_capabilities=desired_caps)


