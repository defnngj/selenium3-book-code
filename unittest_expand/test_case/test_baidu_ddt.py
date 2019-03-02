import unittest
from selenium import webdriver
from time import sleep
from ddt import ddt, data, file_data, unpack

@ddt
class TestBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.base_url = "https://www.baidu.com"

    def baidu_search(self, search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys(search_key)
        self.driver.find_element_by_id("su").click()
        sleep(3)

    # 参数化使用方式一
    @data(["case1", "selenium"], ["case2", "ddt"], ["case3", "python"])
    @unpack
    def test_search1(self, case, search_key):
        print("第一组:用例：", case)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    # 参数化使用方式二
    @data(("case1", "selenium"), ("case2", "ddt"), ("case3", "python"))
    @unpack
    def test_search2(self, case, search_key):
        print("第二组:用例：", case)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    # 参数化使用方式三
    @data({"search_key": "selenium"}, {"search_key": "ddt"}, {"search_key": "python"})
    @unpack
    def test_search3(self, search_key):
        print("第三组:用例：", search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    # 参数化读取JSON文件
    @file_data('ddt_data_file.json')
    def test_search4(self, search_key):
        print("第四组:用例：", search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    # 参数化读取yaml文件
    @file_data('ddt_data_file.yaml')
    def test_search5(self, case):
        search_key = case[0]["search_key"]
        print("第五组:用例：", search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
