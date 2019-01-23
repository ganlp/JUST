#coding=utf-8
from config import globalparam
import os

class Page(object):
    """
    This is a base page class for Page Object.
    """
    def __init__(self, selenium_driver):
        self.dr = selenium_driver
    
    def save_img(self,img_name):
        """
            传入一个img_name, 并存储到默认的文件路径下
            :param img_name:
            :return:
        """
        self.dr.take_screenshot(os.path.join(globalparam.img_path, "ERROR", img_name+".png"))
        

