#coding=utf-8

import os
import sys
sys.path.append('..')
#sys.path.append(rootPath+"public")
from public.common.readconfig import ReadConfig

# 读取配置文件
config_file_path = os.path.split(os.path.realpath(__file__))[0]
read_config = ReadConfig(os.path.join(config_file_path,'config.ini'))
# 项目参数设置
prj_path = read_config.getValue('projectConfig','project_path')

# 日志路径
log_path = os.path.join(prj_path,'JustCC', 'report', 'log')
# 截图文件路径
img_path = os.path.join(prj_path,'JustCC', 'report', 'image')
# 测试报告路径
report_path = os.path.join(prj_path, 'JustCC','report', 'testreport')
# 默认浏览器
browser = 'Chrome'
#默认服务器地址
server_addr="http://192.168.9.248"

# 测试数据路径
data_path = os.path.join(prj_path,'JustCC', 'data', 'testdata')

#用例路径
case_path=os.path.join(prj_path,'JustCC','testcase')

#case_name.json存放路径
json_path=os.path.join(prj_path,'apps','casemanage','static','wdTree','data')

#cookie存放路径
cookie_path_userweb=os.path.join(prj_path,'JustCC','public','common','cookie_userweb.txt')
cookie_path_admin=os.path.join(prj_path,'JustCC','public','common','cookie_admin.txt')

#run.py路径
run_path=os.path.join(prj_path,'JustCC','run.py')

#run_sipp路径：
sipp_path=os.path.join(prj_path,'JustCC','sip_cdr','run_sipp.py')

#server_database数据库信息：
db = {"ip": "192.168.9.248", "loginname": "justtest", "password": "test123", "basename": "organize"}

if __name__=='__main__':
    print(json_path)
    print(db["ip"])
    print(config_file_path)



