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
                    filemode='a'
                    )


mysql_host=''
mysql_port=''
mysql_user=''
mysql_passwd=''
mysql_name=''




#邮件配置
sender_user = '15701374212@163.com'     #发件人邮箱
sender_passwd = '1351668Ao'             #发件人客户端授权码
receivers = '1064420684@qq.com'         #收件人邮箱
smtp_ssl_server = 'smtp.163.com'        #发件人服务器地址
subject = '接⼝测试报告'                  #邮件主题


if __name__=='__main__':
    logging.info("hellow")






























