#coding=utf-8
from config.config_logs import *
import json



def test_case_logging(case_name,url,data,excepct_res,response,res):
    if isinstance(data,dict):
        data=json.dumps(data,ensure_ascii=False)

    logging.info("测试用例:'{}".format(case_name))
    logging.info("url:'{}".format(url))
    logging.info("data:'{}".format(data))
    logging.info("期望结果:'{}".format(excepct_res))
    logging.info("实际结果:'{}".format(response['result']))
    logging.info("实际结果所有信息:'{}".format(res))

