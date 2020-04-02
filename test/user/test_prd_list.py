#coding=utf-8
import unittest
from lib.case_logs import *
import requests
from lib.read_excel import *
from config.config_logs import *
import json
import sys
sys.path.append("../..")


class test_case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
#        cls.data_list=read_excel_data_list(r"/Users/aoxing/PycharmProjects/untitled3/rq_test1/data/test_user_data.xlsx","Test_User_Reng")
        cls.data_list=read_excel_data_list(os.path.join(data_path,'test_user_data.xlsx'),"Test_Prd_List")

    @classmethod
    def tearDownClass(cls):
        pass
    def test_prd_list_normal(self):
        case_data=get_excel_case_data(self.data_list,'test_prd_list_normal')
        if not case_data:
            return '用例不存在'

        url=case_data.get('url')
        data=case_data.get('data')
        #将字符串转为字典
        data_dict=json.loads(data)

        expect_res=int(case_data.get('expect_res'))
        res=requests.post(url=url,data=data_dict)
        response=res.json()

        self.assertEqual(expect_res,response['result'])
        test_case_logging(case_data,url,data,expect_res,response)

    def test_prd_list_nologin(self):
        case_data = get_excel_case_data(self.data_list, 'test_prd_list_nologin')
        if not case_data:
            return '用例不存在'

        url = case_data.get('url')
        data = case_data.get('data')
        # 将字符串转为字典
        data_dict = json.loads(data)

        expect_res = int(case_data.get('expect_res'))
        res = requests.post(url=url, data=data_dict)
        response = res.json()

        self.assertEqual(expect_res, response['result'])
        test_case_logging(case_data, url, data, expect_res, response)

    def test_prd_list_nouserId(self):
        case_data = get_excel_case_data(self.data_list, 'test_prd_list_nouserId')
        if not case_data:
            return '用例不存在'

        url = case_data.get('url')
        data = case_data.get('data')
        # 将字符串转为字典
        data_dict = json.loads(data)

        expect_res = int(case_data.get('expect_res'))
        res = requests.post(url=url, data=data_dict)
        response = res.json()

        self.assertEqual(expect_res, response['result'])
        test_case_logging(case_data, url, data, expect_res, response)

    def test_prd_list_wrongstatus(self):
        case_data = get_excel_case_data(self.data_list, 'test_prd_list_wrongstatus')
        if not case_data:
            return '用例不存在'

        url = case_data.get('url')
        data = case_data.get('data')
        # 将字符串转为字典
        data_dict = json.loads(data)

        expect_res = int(case_data.get('expect_res'))
        res = requests.post(url=url, data=data_dict)
        response = res.json()

        self.assertEqual(expect_res, response['result'])
        test_case_logging(case_data, url, data, expect_res, response)

