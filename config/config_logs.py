#coding=utf-8
import logging
import json
import os
from datetime import datetime


nowtime=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
prj_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_path=os.path.join(prj_path,'data')
test_path=os.path.join(prj_path,'test')

log_file=os.path.join(prj_path,'log','log.txt')
report_file=os.path.join(prj_path,'report',nowtime+' Report.html')

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s,%(lineno)d],%(message)s',
                    datefmt='%Y-%m-%d  %H-%M-%S',
                    filename=log_file,
                    )
mysql_host=''
mysql_port=''
mysql_user=''
mysql_passwd=''
mysql_name=''

if __name__=='__main__':
    logging.info("hellow")






























