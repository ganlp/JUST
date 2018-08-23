__author__ = 'Administrator'
import sys
sys.path.append('../..')
from config import globalparam
'''
1、清空image文件夹
'''

import os
def del_image_file(path): #清空image文件夹
    for i in os.listdir(path):
        path_file=os.path.join(path,i)
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            del_image_file(path_file)

if __name__=='__main__':
    del_image_file(globalparam.img_path)

