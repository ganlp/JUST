__author__ = 'ganlp'

import sys
sys.path.append('../..')
from public.common.basepage import Page
from config import globalparam
from time import sleep
import os
import pymysql
from BeautifulReport import BeautifulReport

class ExtenPage(Page):
    @BeautifulReport.add_test_img('exten', 'addexten')
    def add_exten(self,name,password):
        self.dr.click("xpath->//*[@id=\"fpbx-menu-collapse\"]/ul/li[3]/a")
        sleep(1)
        self.dr.click("xpath->//*[@id=\"fpbx-menu-collapse\"]/ul/li[3]/ul/li[3]/a")
        self.dr.click("xpath->//*[@id=\"toolbar-pjsip\"]/a[1]")
        self.dr.type("xpath->//*[@id=\"extension\"]",name)
        self.dr.clear_type("xpath->//*[@id=\"devinfo_secret\"]",password)
        self.dr.click("xpath->//*[@id=\"submit\"]")
        self.dr.take_screenshot(os.path.join(globalparam.img_path,"exten","addexten.png"))
        sleep(2)
        db = pymysql.connect(globalparam.db_asterisk["ip"], globalparam.db_asterisk["loginname"],
                             globalparam.db_asterisk["password"], globalparam.db_asterisk["basename"], charset='utf8')
        cursor = db.cursor()
        count=cursor.execute("select * from users where extension="+name)
        db.close()
        return count

    @BeautifulReport.add_test_img('exten', 'delexten')
    def del_exten(self):
        self.dr.click("xpath->//*[@id=\"fpbx-menu-collapse\"]/ul/li[3]/a")
        sleep(2)
        self.dr.wait(3)
        self.dr.click("xpath->//*[@id=\"fpbx-menu-collapse\"]/ul/li[3]/ul/li[3]/a")
        tables=self.dr.origin_driver.find_element_by_xpath("//*[@id=\"pjsip_generic\"]/div[1]/div[2]")
        rows1 = tables.find_elements_by_tag_name("tr")
        rows1[0].find_element_by_xpath("//*[@id=\"table-pjsip\"]/tbody/tr[1]/td[5]/a[2]/i").click()
        self.dr.wait(2)
        self.dr.accept_alert()
        sleep(2)
        tables = self.dr.origin_driver.find_element_by_xpath("//*[@id=\"pjsip_generic\"]/div[1]/div[2]")
        rows2 = tables.find_elements_by_tag_name("tr")
        self.dr.take_screenshot(os.path.join(globalparam.img_path, "exten", "delexten.png"))
        return [len(rows1), len(rows2)]

    @BeautifulReport.add_test_img('exten', 'modifyexten')
    def modify_exten(self):
        self.dr.click("xpath->//*[@id=\"fpbx-menu-collapse\"]/ul/li[3]/a")
        sleep(1)
        self.dr.click("xpath->//*[@id=\"fpbx-menu-collapse\"]/ul/li[3]/ul/li[3]/a")
        tables=self.dr.origin_driver.find_element_by_xpath("//*[@id=\"pjsip_generic\"]/div[1]/div[2]")
        rows1 = tables.find_elements_by_tag_name("tr")
        rows1[0].find_element_by_xpath("//*[@id=\"table-pjsip\"]/tbody/tr[1]/td[5]/a[1]/i").click()
        sleep(2)
        self.dr.click("xpath->//*[@id=\"trunk\"]")
        #self.dr.click("xpath->//*[@id=\"trunk\"]/option[2]")
        self.dr.click("xpath->//*[@id=\"submit\"]")
        sleep(2)
        self.dr.take_screenshot(os.path.join(globalparam.img_path, "exten", "modifyexten.png"))


if __name__=='__main__':
    db = pymysql.connect(globalparam.db_asterisk["ip"], globalparam.db_asterisk["loginname"],
                         globalparam.db_asterisk["password"], globalparam.db_asterisk["basename"], charset='utf8')
    cursor = db.cursor()
    count = cursor.execute("select * from users where extension=1001")
    print(count)


