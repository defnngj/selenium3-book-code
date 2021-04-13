"""
测试HTML5页面 -- 无效
"""
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://videojs.com/")

video = driver.find_element_by_id("vjs_video_3_html5_api")

# 返回播放文件地址
url = driver.execute_script("return arguments[0].currentSrc;", video)
print(url)

# 播放视频
print("start")
driver.execute_script("arguments[0].play()", video)

# 播放15秒钟
sleep(15)

# 暂停视频
print("stop")
driver.execute_script("arguments[0].pause()", video)

driver.quit()