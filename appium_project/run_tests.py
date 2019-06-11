import unittest
import time
from HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':
    # 定义测试用例的目录为当前目录
    test_dir = './test_case'
    suit = unittest.defaultTestLoader.discover(start_dir=test_dir,
                                               pattern='test_*.py')

    # 取当前日期时间
    now_time = time.strftime("%Y-%m-%d %H_%M_%S")
    test_report = './test_report/'+now_time+'result.html'
    with(open(test_report, 'wb')) as fp:
        runner = HTMLTestRunner(stream=fp,
                                title="魅族社区APP测试报告",
                                description="运行环境：Android 7.0")
        runner.run(suit)

