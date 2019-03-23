import unittest
import sys
from os.path import dirname, abspath
BASE_PATH = dirname(dirname(abspath(__file__)))
sys.path.append(BASE_PATH)
from common.my_test import MyTest
from page.bbs_page import BBSPage


class TestBBSSearch(MyTest):

    def test_search_meizu_16(self):
        """ 搜索关键字符：魅族16 """
        page = BBSPage(self.driver)
        page.search_box.click()
        page.search_box = u"魅族16"
        page.search_button.click()
        print(page.search_result.text)
        self.assertIn("条帖子", page.search_result.text)


if __name__ == '__main__':
    unittest.main()

