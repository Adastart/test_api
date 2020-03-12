#coding=utf-8
import xlrd
import json

import requests
def read_excel_data_list(file_name,sheet):
    data_list=[]
    wb=xlrd.open_workbook(file_name)
    sh=wb.sheet_by_name(sheet)
    header=sh.row_values(0)
    for i in range(1,sh.nrows):
        d=dict(zip(header,sh.row_values(i)))
        data_list.append(d)
    return data_list


def get_excel_case_data(data_list,case_name):
    for case_data in data_list:
        if case_name==case_data['case_name']:
            return case_data


if __name__=='__main__':
    data_list=read_excel_data_list(r"/Users/aoxing/PycharmProjects/untitled3/rq_test1/data/test_user_data.xlsx","Test_User_Lend")







 #       print(case_data['case_name'])
#        case_data=get_excel(data_list,case_name)