import time
import unittest
import yagmail
from HTMLTestRunner import HTMLTestRunner


# 把测试报告作为附件发送到指定邮箱。
def send_mail(report):
    yag = yagmail.SMTP(user="testingwtb@126.com",
                       password="a123456",
                       host='smtp.126.com')
    subject = "标题，自动化测试报告"
    contents = "正文，请查看附件。"
    yag.send('testingwtb@126.com', subject, contents, report)
    print('email has send out !')


if __name__ == '__main__':
    # 定义测试用例的目录为当前目录
    test_dir = './test_case'
    suit = unittest.defaultTestLoader.discover(test_dir, pattern='test_baidu_parameterized.py')

    # 取当前日期时间
    now_time = time.strftime("%Y-%m-%d %H_%M_%S")
    html_report = './test_report/' + now_time + 'result.html'
    fp = open(html_report, 'wb')
    # 调用HTMLTestRunner，运行测试用例
    runner = HTMLTestRunner(stream=fp,
                            title="百度搜索测试报告",
                            description="运行环境：Windows 10, Chrome浏览器"
                            )
    runner.run(suit)
    fp.close()
    send_mail(html_report)  # 发送报告
