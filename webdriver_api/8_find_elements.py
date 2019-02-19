"""
*  find_elements_xxx("xx")   定位一组元素
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.cn")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)

# 定位一组元素
texts = driver.find_elements_by_xpath("//div[@tpl='se_com_default']/h3/a")

# 计算匹配结果个数
print(len(texts))

# 循环遍历出每一条搜索结果的标题
for t in texts:
    print(t.text)

driver.quit()
