__author__ = 'Administrator'
import sys
sys.path.append('../..')
from config import globalparam
import pymysql

'''
1、清空image文件夹
2、删除客户资料、用户信息的测试数据
3、删除后台基础测试数据
'''
import os
def del_image_file(path): #清空image文件夹
    for i in os.listdir(path):
        path_file=os.path.join(path,i)
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            del_image_file(path_file)

def del_test_app_info(): #清理前台测试数据
    db = pymysql.connect(globalparam.db_organize["ip"], globalparam.db_organize["loginname"], globalparam.db_organize["password"], globalparam.db_organize["basename"], charset='utf8')
    cursor = db.cursor()
    cursor.execute("delete from org_user where username like 'user%'" )  #删除用户数据
    cursor.execute("delete from org_online where agent_number=1112")   #删除在线表的数据
    cursor.execute("delete from org_department where dept_name like '测试%'")  #删除部门数据
    cursor.execute("delete from org_auth_item where description like 'test%'")
    db.commit()
    db.close()

    db = pymysql.connect(globalparam.db_standard["ip"], globalparam.db_standard["loginname"], globalparam.db_standard["password"],globalparam.db_standard["basename"], charset='utf8')
    cursor = db.cursor()
    cursor.execute("delete from crm_customer where customer_name like '客户%'")  # 删除客户资料测试数据
    cursor.execute("delete from crm_enterprise where enterprise_name like '企业%'")  #删除企业测试数据
    cursor.execute("delete from ticket_main where title like '请假%'")  # 删除工单
    cursor.execute("delete from conf_ticket_type where type_name='请假'")  #删除工单类型
    cursor.execute("delete from conf_workflow where title = '测试流程'")  #删除工作流
    db.commit()
    db.close()

    db = pymysql.connect(globalparam.db_standard["ip"], globalparam.db_standard["loginname"],
                         globalparam.db_standard["password"], globalparam.db_stdout["basename"], charset='utf8')
    cursor = db.cursor()
    cursor.execute("delete from  stdout_task_category  where name like '测试%'")  #删除电销分类
    cursor.execute("delete from stdout_object where object_name like '测试%'") #删除电销项目
    
    db.commit()
    db.close()


def del_test_manage_info(): #清理后台数据
    db = pymysql.connect(globalparam.db_asterisk["ip"], globalparam.db_asterisk["loginname"],globalparam.db_asterisk["password"], globalparam.db_asterisk["basename"], charset='utf8')
    cursor = db.cursor()
    cursor.execute("delete from users where extension like '100%'")  # 删除分机数据
    cursor.execute("delete from devices where id like '100%'")  # 删除分机数据
    cursor.execute("delete from queues_config where extension like '70%'") #删除队列数据
    cursor.execute("delete from queues_details where id like '70%'") #删除队列数据
    cursor.execute("delete from trunks where name like 'trunk%'") #删除中继测试数据
    cursor.execute("delete t1 from pjsip as t1 inner join (SELECT id from pjsip  where keyword='trunk_name' and data like 'trunk%')as t2 on t1.id=t2.id ")
    cursor.execute("delete from incoming where description='callinrule'")  #删除呼入规则
    cursor.execute("delete from outbound_routes where name like 'calloutrule'")  #删除呼出规则
    cursor.execute("delete from outbound_route_patterns where route_id in (SELECT route_id from outbound_routes where name='calloutrule')")
    db.commit()
    db.close()

if __name__=='__main__':
    del_image_file(globalparam.img_path)
    del_test_app_info()
    del_test_manage_info()

