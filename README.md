
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

