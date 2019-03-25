"""
* name			      →		find_element_by_name()
* tag_name            →    find_element_by_tag_name()
* class_name		  →		find_element_by_class_name()
* link_text			  →		find_element_by_link_text()
* partial_link_text   →    find_element_by_partial_link_text()
* xpath				  →	    find_element_by_xpath()
* css_selector        →		find_element_by_css_selector()
"""
from selenium import webdriver

driver = webdriver.Chrome()

# id 定位
driver.find_element_by_id("kw")
driver.find_element_by_id("su")

# name 定位
driver.find_element_by_name("wd")

# class 定位
driver.find_element_by_class_name("s_ipt")

# tag定位
driver.find_element_by_tag_name("input")

# link text定位
driver.find_element_by_link_text("新闻")
driver.find_element_by_link_text("hao123")
driver.find_element_by_link_text("地图")
driver.find_element_by_link_text("视频")
driver.find_element_by_link_text("贴吧")

# partial link定位
driver.find_element_by_partial_link_text("一个很长的")
driver.find_element_by_partial_link_text("文本链接")

# XPath 定位
# 1、绝对路径定位
driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/from/span/input")
driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/from/span[2]/input")

# 2、利用元素属性定位
driver.find_element_by_xpath("//input[@id='kw']")
driver.find_element_by_xpath("//input[@id='su']")
driver.find_element_by_xpath("//*[@name='wd']")
driver.find_element_by_xpath("//*[@class='s_ipt']")
driver.find_element_by_xpath("//input[@maxlength='100']")
driver.find_element_by_xpath("//input[@autocomplete='off']")
driver.find_element_by_xpath("//input[@type='submit']")

# 3、层级与属性结合
driver.find_element_by_xpath("//span[@class='bg s_ipt_wr']/input")
driver.find_element_by_xpath("//form[@id='form']/span/input")
driver.find_element_by_xpath("//form[@id='form']/span[2]/input")

# 4、使用逻辑运算符
driver.find_element_by_xpath("//input[@id='kw' and @class='s_ipt']")

# 5、使用contains方法
driver.find_element_by_xpath("//span[contains(@calss,'s_ipt_wr')]/input")

# 6、使用text()方法
driver.find_element_by_xpath("//a[text(),'新闻')]")

driver.find_element_by_xpath("//a[contains(text(),'一个很长的')]")


# CSS 定位
# 1.通过class属性定位
driver.find_element_by_css_selector(".s_ipt")
driver.find_element_by_css_selector(".s_btn")

# 2、通过id属性定位
driver.find_element_by_css_selector("#kw")
driver.find_element_by_css_selector("#su")

# 3、通过标签名定位
driver.find_element_by_css_selector("input")

# 4、通过标签层级关系定位
driver.find_element_by_css_selector("span > input")

# 5、通过属性定位
driver.find_element_by_css_selector("[autocomplete=off]")
driver.find_element_by_css_selector("[name='kw']")
driver.find_element_by_css_selector('[type="submit"]')

# 6、组合定位
driver.find_element_by_css_selector("form.fm > span > input.s_ipt")
driver.find_element_by_css_selector("form#form > span > input#kw")

# 7、更多定位用法
driver.find_element_by_css_selector("[class*=s_ipt_wr]")
driver.find_element_by_css_selector("[class^=bg]")
driver.find_element_by_css_selector("[class$=wrap]")
driver.find_element_by_css_selector("form > input:nth-child(2)")
