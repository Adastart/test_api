#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from config.config_logs import *

def send_email(report_file):

    msg = MIMEMultipart() # 混合MIME格式
    msg.attach(MIMEText(open(report_file, encoding='utf-8').read(), 'html', 'utf-8')) # 添加html格式邮件正⽂（会丢失css格式）

    msg['From'] =sender_user  # 发件⼈
    msg['To'] =receivers # 收件⼈
    msg['Subject'] = Header(subject, 'utf-8') # 中⽂邮件主题，指定utf-8编码

    att1 = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8') # ⼆进制格式打开
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="report.html"' # filename为邮件中附件显示的名字
    msg.attach(att1)

    try:
        smtp = smtplib.SMTP_SSL(smtp_ssl_server) # smtp服务器地址 使⽤SSL模式
        smtp.login(sender_user, sender_passwd) # ⽤户名和密码(密码是客户端授权码)
        smtp.sendmail(sender_user, receivers,msg.as_string())

        logging.info("邮件发送完成！")
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()


