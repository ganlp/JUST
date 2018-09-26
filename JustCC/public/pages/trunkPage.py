__author__ = 'ganlp'

import sys
sys.path.append('../..')
from public.common.basepage import Page
from config import globalparam
from time import sleep
import os
import pymysql

class TrunkPage(Page):
    def add_trunk(self,name,zone,maxchans,server_ip):
        self.dr.click("xpath->//*[@id=\"fpbx-menu-collapse\"]/ul/li[4]/a")
        sleep(1)
        self.dr.click("xpath->//*[@id=\"fpbx-menu-collapse\"]/ul/li[4]/ul/li[3]/a")
        sleep(1)
        self.dr.click("xpath->//*[@id=\"toolbar-all\"]/div[1]/a/div")
        self.dr.type("xpath->//*[@id=\"trunk_name\"]",name)
        self.dr.type("xpath->//*[@id=\"zone\"]",zone)
        self.dr.type("xpath->//*[@id=\"phonest\"]",name)
        self.dr.click("xpath->//*[@id=\"outcid\"]")
        self.dr.type("xpath->//*[@id=\"maxchans\"]",maxchans)
        self.dr.click("xpath->//*[@id=\"trunkEdit\"]/ul/li[3]/a")
        self.dr.type("xpath->//*[@id=\"username\"]",name)
        sleep(1)
        self.dr.type("css->#secret",name)
        sleep(5)
        self.dr.type("xpath->//*[@id=\"sip_server\"]",server_ip)
        self.dr.click("xpath->//*[@id=\"submit\"]")
        self.dr.take_screenshot(os.path.join(globalparam.img_path, "trunk", "addtrunk.png"))
        db=pymysql.connect(globalparam.db["ip"], globalparam.db["loginname"], globalparam.db["password"], "asterisk")
        cursor = db.cursor()
        count=cursor.execute("select * from trunks where name="+name)
        db.close()
        return count





