#coding=utf-8
import unittest
import logging
import sys
#sys.path.append('../')
sys.path.append('/Users/aoxing/PycharmProjectsa')
print(sys.path)

from config.config_logs import *
from lib.HTMLTestReportCN import HTMLTestRunner
from lib.send_email import *


logging.info("===================================测试开始==================================")

suite=unittest.defaultTestLoader.discover(test_path)

with open(report_file,'wb') as  f:
    HTMLTestRunner(stream=f,title='api_test',description='test',tester='ada').run(suite)

send_email(report_file)
logging.info("===================================测试结束==================================")
