# coding=utf-8
"Combine tests for gnosis.xml.objectify package (req 2.3+)"

import HTMLTestRunner
import doctest,unittest
from test_case.receptionist import Zhinengqiantai_test
from test_case.member import MemberMarketing_test
from test_case.report import OperatingStatement_test
from test_case.setting import Service_test
from test_case.staff import StaffSetting_test

suite = doctest.DocTestSuite()

suite.addTest(unittest.makeSuite(Zhinengqiantai_test.Reception))
suite.addTest(unittest.makeSuite(MemberMarketing_test.Member))
suite.addTest(unittest.makeSuite(OperatingStatement_test.Report))
suite.addTest(unittest.makeSuite(Service_test.Project_Setting))
suite.addTest(unittest.makeSuite(StaffSetting_test.Staff))

filename = 'D:\\py\\test\\result.html'

fp = open(filename, 'wb')
# 定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(
stream=fp,
title='Report_title',
description='Report_description')

runner.run(suite)