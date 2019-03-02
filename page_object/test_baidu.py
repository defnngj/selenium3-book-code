import unittest
from time import sleep
from selenium import webdriver
from baidu_page import BaiduPage


class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def test_baidu_search_case1(self):
        page = BaiduPage(self.driver)
        page.open()
        page.search_input("selenium")
        page.search_button()
        sleep(2)
        self.assertEqual(page.get_title(), "selenium_百度搜索")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
