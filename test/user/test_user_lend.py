#coding=utf-8
import unittest
import requests
from lib.read_excel import *
from lib.case_logs import *
from config.config_mysql import *
from config.config_logs import *
import sys
sys.path.append("../..")

class Test_User_Lend(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
  #      cls.data_list=read_excel_data_list(r"/Users/aoxing/PycharmProjects/untitled3/rq_test1/data/test_user_data.xlsx","Test_User_Lend")
        cls.db=DB()
        cls.data_list=read_excel_data_list(os.path.join(data_path,'test_user_data.xlsx'),"Test_User_Lend")

    @classmethod
    def tearDownClass(cls):
        pass

    def test_user_lend_normal(self):
        case_data=get_excel_case_data(self.data_list,'test_user_lend_normal')
        name=self.db.check_userId(85174)
        logging.info(name)
        if not case_data:
             logging.info('用例不存在')
        url=case_data.get('url')
        data = case_data.get('data')
        print(data)
        expect_res = int(case_data.get('expect_res'))
        res=requests.post(url=url,data=data)
        response=res.json()
        test_case_logging(case_data,url,data,expect_res,response)
        self.assertEqual(response['result'],expect_res)


    def test_user_lend_nologin(self):
        case_data=get_excel_case_data(self.data_list,'test_user_lend_nologin')
        if not case_data:
            logging.info('用例不存在')
        url=case_data.get('url')
        data=case_data.get('data')
        expect_res=int(case_data.get('expect_res'))
        res=requests.post(url=url,data=data)
        response=res.json()
        test_case_logging(case_data,url,data,expect_res,response['result'])
        self.assertEqual(response['result'],expect_res)
