__author__ = 'ganlp'

import sys
sys.path.append('../..')
from public.common.basepage import Page
from config import globalparam
from time import sleep
import os
import pymysql

class CallOutPage(Page):
    def add_calloutrule(self):
        self.dr.click("xpath->//*[@id=\"fpbx-menu-collapse\"]/ul/li[4]/a")
        sleep(1)
        self.dr.click("xpath->//*[@id=\"fpbx-menu-collapse\"]/ul/li[4]/ul/li[2]/a")
        self.dr.click("xpath->//*[@id=\"toolbar-all\"]/a[1]")
        self.dr.type("xpath->//*[@id=\"routename\"]","calloutrule")
        self.dr.click("xpath->//*[@id=\"trunkpri0\"]")
        self.dr.wait(2)
        self.dr.click("xpath->//*[@id=\"trunkpri0\"]/option[2]")
        self.dr.click("xpath->//*[@id=\"routeEdit\"]/ul/li[2]/a")
        self.dr.type("xpath->//*[@id=\"pattern_pass_0\"]",'X.')
        self.dr.click("xpath->//*[@id=\"submit\"]")
        self.dr.take_screenshot(os.path.join(globalparam.img_path,"calloutrule","add_calloutrule.png"))
        sleep(2)
        db = pymysql.connect(globalparam.db_asterisk["ip"], globalparam.db_asterisk["loginname"],
                             globalparam.db_asterisk["password"], globalparam.db_asterisk["basename"], charset='utf8')
        cursor = db.cursor()
        count=cursor.execute("select * from outbound_routes where name='calloutrule'")
        db.close()
        return count



