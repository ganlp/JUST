__author__ = 'ganlp'

import sys
sys.path.append('../..')
from public.common.basepage import Page
from config import globalparam
from time import sleep
import os
import pymysql

class queuePage(Page):
    def add_queue(self,name):
        self.dr.click("xpath->//*[@id=\"fpbx-menu-collapse\"]/ul/li[3]/a")
        sleep(1)
        self.dr.click("xpath->//*[@id=\"fpbx-menu-collapse\"]/ul/li[3]/ul/li[10]/a")
        sleep(2)
        self.dr.click("xpath->//*[@id=\"toolbar-all\"]/a")
        self.dr.type("xpath->//*[@id=\"account\"]",name)
        self.dr.type("xpath->//*[@id=\"name\"]",name)
        self.dr.click("xpath->//*[@id=\"goto0\"]")
        self.dr.click("xpath->//*[@id=\"goto0\"]/option[9]")
        self.wait(2)
        self.dr.click("xpath->//*[@id=\"submit\"]")
        sleep(2)
        self.dr.take_screenshot(os.path.join(globalparam.img_path, "queue", "addqueue.png"))
        db=pymysql.connect(globalparam.db["ip"], globalparam.db["loginname"], globalparam.db["password"], "asterisk")
        cursor = db.cursor()
        count=cursor.execute("select * from queues_config where extension=901")
        db.close()
        return count






