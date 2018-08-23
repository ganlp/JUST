#coding:utf-8

import os
import time
import sys
sys.path.append('../..')
from public.common.log import Log
from config import globalparam
import yagmail


# 测试报告的路径
reportPath = globalparam.report_path
logger = Log()
# 配置收发件人
recvaddress = ['ganlp@justcall.cn']  #,'1053995075@qq.com'
sendaddr_name = 'ganlp@justcall.cn'
sendaddr_pswd = '200913138003'
mail_server='mail.justcall.cn'
Subject='测试报告主题'

class SendMail:
    def get_report(self):
        #获取最新测试报告
        dirs = os.listdir(reportPath)
        dirs.sort()
        newreportname = dirs[-1]
        print('The new report name: {0}'.format(newreportname))
        return newreportname

    def send(self):
        #发送邮件
        newreport=self.get_report()
        # with open(os.path.join(reportPath,newreport), 'rb') as f:
        #     mailbody = f.read()
        #     print(mailbody)
        mailbody="报告详情请见附件"
        try:
            yag=yagmail.SMTP(user=sendaddr_name,password=sendaddr_pswd,host=mail_server)
            yag.send(recvaddress,Subject,contents=[mailbody,os.path.join(reportPath,newreport)])
            logger.info("发送邮件成功")
        except Exception:
            logger.error('发送邮件失败')
            raise

if __name__ == '__main__':
	sendMail = SendMail()
	sendMail.send()

        
