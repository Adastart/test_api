#coding=utf-8
import requests
import json
from config.config_logs import *
# #x-www.form-urlencodie
# url='https://test.weiyangpuhui.com/if/plan/capitalInfo/productList.htm'
# data={"userId":"85174","token":"49e42d6f6b9a48b89d4cff03a86ea822","status":"1","page":"1","rows":"4"}
#
# res=requests.post(url=url,data=data)
# print(res.text)
# print(type(data))
#
# #json
# url1='https://test.weiyangpuhui.com/if/plan/capitalOrder/save.htm'
# data1='''{"userId":"85175","token":"2f9f6003bbc34d8c866e87cd11d4adc2","planProductId":"10243","investAmt":"100"}'''
# dataw={"userId":"85175","token":"2f9f6003bbc34d8c866e87cd11d4adc2","planProductId":"10243","investAmt":"100"}
# resaw=requests.post(url=url1,data=dataw)
# print(resaw.text)

def exit_prd(userid,token):


    #获取加入整存宝列表
    urlgetlist = 'https://test.weiyangpuhui.com/if/plan/capitalOrder/myPlanOrders.htm'
    datagetlist = {"userId": userid, "token": token, "status": "1"}
    res = requests.post(url=urlgetlist, data=datagetlist)
    response=res.json()
    #字典格式取值
    res_1=response.get('data').get('data')
    print(type(res_1))
    print(res_1)
    '''
    #列表格式取值
    
    res_list_id=res_1[2]['id']
    print(type(res_list_id))
    
    
    
    
    #取消整存宝
    urlexit = 'https://test.weiyangpuhui.com/if/plan/capitalOrder/exitPlan.htm'
    dataexit = {"userId": userid, "token": token,"id":res_list_id}
    
    res_exit=requests.post(url=urlexit,data=dataexit)
    print(res_exit.text)
    
    '''

    for i in range (0,len(res_1)):
        # print(i)
        # print(res_1[i])
        res_i_id=(res_1[i]['id'])
        urlexit = 'https://test.weiyangpuhui.com/if/plan/capitalOrder/exitPlan.htm'
        dataexit = {"userId": userid, "token": token,"id":res_i_id}

        res_exit=requests.post(url=urlexit,data=dataexit)
        print(res_exit.text)
    return  print(res_exit.text)
    logging.info(res_exit.text)
if __name__=='__main__':
    exit_prd(userid='85175',
             token='2f9f6003bbc34d8c866e87cd11d4adc2')