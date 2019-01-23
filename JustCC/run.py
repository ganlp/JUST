#coding=utf-8

import unittest
import HTMLTestRunner
import time,json
from config import globalparam
from public.common import sendmail_2
from public.common import initialize
from public.common import login
from testcase import test_10_login_staticlogin,test_20_organize_depart,test_22_organize_user,test_30_call_toolbar,test_60_admin_trunk,test_61_admin_exten,test_62_admin_queue,test_40_customerMag_customer,\
    test_63_admin_callinrule,test_64_admin_calloutrule,test_50_ticket_ticket,test_21_organize_role
import os
from BeautifulReport import BeautifulReport


file_list=os.listdir(globalparam.case_path)
for file in file_list:
    if(file[:4]=="test"):
        modulename=file[:-3]
    #	importlib.import_module(eval(modulename))

def getSuite(testlevel):
    """构造测试集"""
    if testlevel==1:  #一级测试用例优先级最高
        suite=unittest.TestSuite()
        with open(globalparam.json_path+"\\casedata2.json","rb") as f:
            load_dict=json.load(f)
        for i in load_dict:
            filename=i['filename']
            classname=i['class']
            for j in i['case']:
                suite.addTest(eval(filename+'.'+classname)(j['id']))
        # case_dict=case.Case().get_case_name()
        # for key,value in case_dict.items():
        #     for i in range(1,len(value)):
        #         suite.addTest(eval(key+'.'+value[0])(value[i]))     #eval函数可以将字符串转为可执行命令
        # suite.addTest(test_1_login.Login("test_static_login"))  #静态登录
        return suite

def run():
  #  test_dir = './testcase'
  #  suite = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')  按格式匹配加入测试集的测试用例
    suite=getSuite(1)
    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    initialize.del_image_file(globalparam.img_path)
    initialize.del_test_app_info()
    initialize.del_test_manage_info()
    lg=login.Login()
    lg.login()
    lg.login_admin()
  
    #######################使用HTMLTestRunner模板#############
    # reportname = globalparam.report_path + '\\' + 'TestResult' + now + '.html'
    # with open(reportname,'wb') as f:
    #     runner = HTMLTestRunner.HTMLTestRunner(
    #         stream=f,
    #         title='测试报告',
    #         description='Test the import testcase'
    #     )
    #     runner.run(suite)
    ##########################################################
  
  
   ###################使用BeautifulReport模板########################
    result = BeautifulReport(suite)
    result.report(filename='TestResult'+ now, description="智能版基础用例", log_path=globalparam.report_path)
   ##################################################################
   
    time.sleep(3)
    # 发送邮件
    mail = sendmail_2.SendMail()
    mail.send()

if __name__=='__main__':
    run()