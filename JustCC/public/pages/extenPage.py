__author__ = 'ganlp'

import sys
sys.path.append('../..')
from public.common.basepage import Page
from config import globalparam
from time import sleep
import os
import pymysql

class ExtenPage(Page):
    def add_exten(self):
        self.dr.click("xpath->//*[@id=\"fpbx-menu-collapse\"]/ul/li[3]/a")
        sleep(1)
        self.dr.click("xpath->//*[@id=\"fpbx-menu-collapse\"]/ul/li[3]/ul/li[3]/a")
        self.dr.click("xpath->//*[@id=\"toolbar-pjsip\"]/a[1]")
        self.dr.type("xpath->//*[@id=\"extension\"]",'1001')
        self.dr.type("xpath->//*[@id=\"devinfo_secret\"]",'1001')
        self.dr.click("xpath->//*[@id=\"submit\"]")
        self.dr.take_screenshot(os.path.join(globalparam.img_path,"exten","addexten.png"))
        sleep(2)
        db=pymysql.connect(globalparam.db["ip"], globalparam.db["loginname"], globalparam.db["password"], "asterisk")
        cursor = db.cursor()
        count=cursor.execute("select * from users where extension=1001")
        db.close()
        return count

    def del_exten(self):
        self.dr.click("xpath->//*[@id=\"fpbx-menu-collapse\"]/ul/li[3]/a")
        sleep(1)
        self.dr.click("xpath->//*[@id=\"fpbx-menu-collapse\"]/ul/li[3]/ul/li[3]/a")
        tables=self.dr.origin_driver.find_element_by_xpath("//*[@id=\"pjsip_generic\"]/div[1]/div[2]")
        rows1 = tables.find_elements_by_tag_name("tr")
        rows1[0].find_element_by_xpath("//*[@id=\"table-pjsip\"]/tbody/tr[1]/td[5]/a[2]/i").click()
        sleep(5)
        tables = self.dr.origin_driver.find_element_by_xpath("//*[@id=\"pjsip_generic\"]/div[1]/div[2]")
        self.dr.dismiss_alert()
        sleep(15)
        rows2 = tables.find_elements_by_tag_name("tr")
        return [len(rows1), len(rows2)]

if __name__=='__main__':
    db = pymysql.connect(globalparam.db["ip"], globalparam.db["loginname"], globalparam.db["password"], "asterisk")
    cursor = db.cursor()
    count = cursor.execute("select * from users where extension=1001")
    print(count)


