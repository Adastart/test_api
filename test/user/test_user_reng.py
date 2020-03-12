#coding=utf-8
import unittest
from lib.case_logs import *
import requests
from lib.read_excel import *
from config.config_logs import *
import sys
sys.path.append("../..")


class test_case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
#        cls.data_list=read_excel_data_list(r"/Users/aoxing/PycharmProjects/untitled3/rq_test1/data/test_user_data.xlsx","Test_User_Reng")
        cls.data_list=read_excel_data_list(os.path.join(data_path,'test_user_data.xlsx'),"Test_User_Reng")

    @classmethod
    def tearDownClass(cls):
        pass
    def test_user_reng_normal(self):
        case_data=get_excel_case_data(self.data_list,'test_user_reng_normal')
        if not case_data:
            return '用例不存在'

        url=case_data.get('url')
        data=case_data.get('data')
        expect_res=int(case_data.get('expect_res'))
        res=requests.post(url=url,data=data)
        response=res.json()


        self.assertEqual(expect_res,response['result'])
        test_case_logging(case_data,url,data,expect_res,response)

    def test_user_reng_nologin(self):
        case_data = get_excel_case_data(self.data_list, 'test_user_reng_nologin')
        if not case_data:
            return '用例不存在'

        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = int(case_data.get('expect_res'))
        res = requests.post(url=url, data=data)
        response = res.json()
        self.assertEqual(expect_res, response['result'])
        test_case_logging(case_data,url,data,expect_res,response)

