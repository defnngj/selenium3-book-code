
## 介绍

[《Selenium3自动化测试实战--基于Python语言》](https://item.jd.com/51066091172.html) 书中源码。


## 书中错误
注：p代表page, 10 代表页数

#### p46

绝对路径定位：
```python
find_element_by_xpath("/html/body/div/div[2]/div/div/div/from/span/input")
find_element_by_xpath("/html/body/div/div[2]/div/div/div/from/span[2]/input")
```
修改为：
```python
find_element_by_xpath("/html/body/div/div[2]/div/div/div/form/span/input")
find_element_by_xpath("/html/body/div/div[2]/div/div/div/form/span[2]/input")
```

#### p48

* text()的使用

错误一

```python
find_element_by_xpath("//a[text(), '新闻']")
```

修改为：
```
find_element_by_xpath("//a[text()='新闻']")
```

错误二

```python
find_element_by_xpath("//a[contains(text(), '一个很长的')]")
```

修改为：

```python
find_element_by_xpath("//a[contains(text()='一个很长的')]")
```


#### p54

submit()的使用例子：
```python
seearch.submit()
```
修改为：
```python
search_text.submit()
```

#### p60

判断元素是否显示，实例用用的`visibility_of_element_located`方法，但是解释部分用的`presence_of_element_located`方法。

* `visibility_of_element_located` 表示检查元素是否存在于页面和可见。
* `presence_of_element_located` 表示检查页的DOM上是否存在期望的元素。

#### p69

4.12 小节下拉框处理

由于百度搜索设置页面修改，例子失效，现换成w3school网站例子。

```python
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.w3school.com.cn/tiy/t.asp?f=eg_html_select')
driver.set_page_load_timeout(2)
driver.set_script_timeout(2)

# 切换表单
driver.switch_to.frame("iframeResult")

# 定位select标签
sel = driver.find_element_by_tag_name("select")

# value="saab"
Select(sel).select_by_value('saab')
sleep(2)

# <option>Opel</option>
Select(sel).select_by_visible_text("Opel")
sleep(2)

# 根据选项的索引选择
Select(sel).select_by_index(3)
sleep(2)

driver.quit()
```

#### p79 ~ 81
4.18 小节 滑动解锁 

1. 滑动解锁的例子失效，暂未找到很好的替代的例子，新印刷版中去掉。
2. 标题修改为"滑动操作"
3. 滑动操作日历的例子替换为：

```python
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
```


#### p86

5.3 小节模块化与参数化 （不做修改）

126邮箱登录的例子已经失效，读者体会例子设计思路即可。

目前大部分网站都有验证码等安全机制，给我们做自动化带来了一定的难度。最好的方式是和公司开发一起淘率解决方案。

* 设置万能码

* 设置隐藏关闭验证码功能

#### p92

5.4.3 小节读取xml文件

`config.xml`文件，标签错误。
```xml
    <platform>
        <os>Windows</os>
        <os>Linux</os>
        <os>macOS</os>
    <platform>
```
修改为：
```xml
    <platform>
        <os>Windows</os>
        <os>Linux</os>
        <os>macOS</os>
    </platform>
```
