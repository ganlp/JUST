__author__ = 'ganlp'

import sys
sys.path.append('../..')
from public.common.basepage import Page
from config import globalparam
from time import sleep
import os
import pymysql
from BeautifulReport import BeautifulReport

class CallInPage(Page):
    @BeautifulReport.add_test_img('callinrule', 'add_callinrule')
    def add_callinrule(self):
        self.dr.click("xpath->//*[@id=\"fpbx-menu-collapse\"]/ul/li[4]/a")
        sleep(1)
        self.dr.click("xpath->//*[@id=\"fpbx-menu-collapse\"]/ul/li[4]/ul/li[1]/a")
        self.dr.click("xpath->//*[@id=\"toolbar-all\"]/a")
        self.dr.wait(2)
        self.dr.type("xpath->//*[@id=\"description\"]","callinrule")
        self.dr.click("xpath->//*[@id=\"didgeneral\"]/div[2]/div[2]/div/div/div/div/div[2]/select")
        self.dr.wait(2)
        self.dr.click("xpath->//*[@id=\"didgeneral\"]/div[2]/div[2]/div/div/div/div/div[2]/select/option[2]")
        self.dr.click("xpath->//*[@id=\"extension\"]")
        self.dr.click("xpath->//*[@id=\"extension\"]/option[2]")
        self.dr.click("xpath->//*[@id=\"submit\"]")
        self.dr.take_screenshot(os.path.join(globalparam.img_path,"callinrule","add_callinrule.png"))
        sleep(2)
        db = pymysql.connect(globalparam.db_asterisk["ip"], globalparam.db_asterisk["loginname"],
                             globalparam.db_asterisk["password"], globalparam.db_asterisk["basename"], charset='utf8')
        cursor = db.cursor()
        count=cursor.execute("select * from incoming where description='callinrule'")
        db.close()
        return count



