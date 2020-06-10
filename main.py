import unittest, time, os
from HTMLTestRunner import HTMLTestRunner

testcase_path = "./testcase"
# 报告存放的文件夹
report_path = './report/'
# 报告命名加上时间格式化
now = time.strftime('%Y-%m-%d %H_%M_%S')
# 报告文件名称
report_file = report_path + now + 'report.html'
# 测试报告标题
report_title = 'WEB自动化测试报告'
# 测试报告描述
report_desc = 'WEB自动化测试报告详细情况'
# 判断存放报告的文件夹是否存在，如果不存在则创建
if not os.path.exists(report_path):
    os.mkdir(report_path)

# 生产测用例套件
def creat_suite():
    uit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(testcase_path, pattern="test_*.py")
    for test_suite in discover:
        # print(test_suite)
        for test_case in test_suite:
            uit.addTest(test_case)
    return uit


suite = creat_suite()
# 打开文件，写入测试结果
with open(report_file, 'wb') as report:
    # 使用HTMLTestRunner运行测试套件
    runner = HTMLTestRunner(stream=report, verbosity=2, title=report_title, description=report_desc)
    runner.run(suite)
report.close()
