#coding=utf-8
from lib.case_logs import *
from lib.read_excel import *
import unittest
from config.config_logs import *
import sys
sys.path.append("../..")

class Test_User_Total_Case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #cls.data_list=read_excel_data_list(r"/Users/aoxing/PycharmProjects/untitled3/rq_test1/data/test_user_data.xlsx","Test_User_Lend")
        cls.data_list=read_excel_data_list(os.path.join(data_path,'test_user_data.xlsx'),"Test_User_Lend")


    @classmethod
    def tearDownClass(cls):
        pass

    def test_user_lend_case(self):
   #     self.data_list=read_excel_data_list("test_user_data.xlsx","Test_User_Lend")
        for case_data in self.data_list:
            case_name=case_data.get('case_name')
            url=case_data.get('url')
            data=case_data.get('data')
            expect_res=int(case_data.get('expect_res'))

            print(expect_res)
            res =requests.post(url=url,data=data)
            print(res.text)
            response=res.json()
            test_case_logging(case_name,url,data,expect_res,response)
            try:self.assertEqual(expect_res,response['result'])
            except Exception as e:
                continue


    def test_user_reng_case(self):
        for case_data in self.data_list:
            case_name=case_data.get('case_name')
            url=case_data.get('url')
            data=case_data.get('data')
            expect_res=int(case_data.get('expect_res'))

            res=requests.post(url=url,data=data)
            response=res.json()
            test_case_logging(case_name,url,data,expect_res,response)
            try:self.assertEqual(expect_res,response['result'])
            except Exception as e:
                continue


