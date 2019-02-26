import unittest


def setUpModule():
    print("test module start >>>>>>>>>>>>>>")


def tearDownModule():
    print("test module end >>>>>>>>>>>>>>")


class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("test class start =======>")

    @classmethod
    def tearDownClass(cls):
        print("test class end  =======>")

    def setUp(self):
        print("test case start -->")

    def tearDown(self):
        print("test case end -->")

    def test_case1(self):
        print("test case1")

    def test_case2(self):
        print("test case2")


if __name__ == '__main__':
    unittest.main()
