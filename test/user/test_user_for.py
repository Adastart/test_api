#coding=utf-8
from lib.case_logs import *
from lib.read_excel import *
import unittest
from config.config_logs import *
import json
import sys
sys.path.append("../..")

class Test_User_Total_Case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #cls.data_list=read_excel_data_list(r"/Users/aoxing/PycharmProjects/untitled3/rq_test1/data/test_user_data.xlsx","Test_User_Lend")
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_user_lend_case(self):
        self.data_list = read_excel_data_list(os.path.join(data_path, 'test_user_data.xlsx'), "Test_User_Lend")

#     self.data_list=read_excel_data_list("test_user_data.xlsx","Test_User_Lend")
        for case_data in self.data_list:
            case_name=case_data.get('case_name')
            url=case_data.get('url')
            data=case_data.get('data')
            data_dict=json.loads(data)
            print(type(data))
            expect_res=int(case_data.get('expect_res'))
            print(expect_res)
            res =requests.post(url=url,data=data_dict)
            print(res.text)
            response=res.json()

            test_case_logging(case_data, url, data, expect_res, response, res.text)
            try:self.assertEqual(expect_res,response['result'])
            except Exception as e:
                continue


    def test_prd_list_case(self):
        self.data_list = read_excel_data_list(os.path.join(data_path, 'test_user_data.xlsx'), "Test_Prd_List")
        for case_data in self.data_list:
            case_name=case_data.get('case_name')
            url=case_data.get('url')
            data=case_data.get('data')
            data_dict=json.loads(data)

            expect_res=int(case_data.get('expect_res'))
            print(expect_res)
            res=requests.post(url=url,data=data_dict)
            response=res.json()
            print(res.text)
            test_case_logging(case_data, url, data, expect_res, response, res.text)
            try:self.assertEqual(expect_res,response['result'])
            except Exception as e:
                continue


