#coding=utf-8
import unittest
from HTMLTestReportCN import *
import logging
import sys
sys.path.append('..')
from config_logs import *



logging.info("===================================测试开始==================================")

suite=unittest.defaultTestLoader.discover(test_path)

with open(report_file,'wb') as  f:
    HTMLTestRunner(stream=f,title='api_test',description='test',tester='ada').run(suite)

logging.info("===================================测试结束==================================")
