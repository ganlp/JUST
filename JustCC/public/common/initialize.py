__author__ = 'Administrator'
import sys
sys.path.append('../..')
from config import globalparam
import pymysql

'''
1、清空image文件夹
2、删除org_user表的测试数据
'''

import os
def del_image_file(path): #清空image文件夹
    for i in os.listdir(path):
        path_file=os.path.join(path,i)
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            del_image_file(path_file)

def del_test_user_info():
    db = pymysql.connect(globalparam.db["ip"], globalparam.db["loginname"], globalparam.db["password"], globalparam.db["basename"])
    cursor = db.cursor()
    cursor.execute("delete from org_user where username like 'user%'" )
    cursor.execute("delete from org_online")
    db.commit()
    db.close()


if __name__=='__main__':
    del_image_file(globalparam.img_path)
    del_test_user_info()

