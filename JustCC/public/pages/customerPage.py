import sys
sys.path.append('../..')
from public.common.basepage import Page
from time import sleep
from selenium.webdriver.common.keys import Keys
from config import globalparam
import os
import random
import pymysql

class CustomerPage(Page):
    def add_customer(self):
     #   self.dr.click("xpath->//*[@id=\"sidebar\"]/ul/li/div/a[12]/span")
     #   self.dr.click("css->#sidebar > ul > li > div > a:nth-child(15) > span")
        self.dr.click("link_text->客户管理")
        self.dr.wait(1)
        self.dr.click("link_text->客户资料")
        self.dr.switch_to_frame("id->iframe_standard_crm_customer_index")
        #tables=self.dr.origin_driver.find_element_by_xpath("//*[@id=\"customer-grid\"]/div[1]/table")
        #rows1 = len(tables.find_elements_by_tag_name('tr'))
        self.dr.click("xpath->/html/body/div/header/div[2]/a")
        sleep(2)
        self.dr.switch_to_frame_out()
        self.dr.switch_to_frame("id->iframe_standard_crm_customer_create")
        self.dr.type("xpath->//*[@id=\"customer-customer_name\"]","客户2")
        self.dr.click("xpath->//*[@id=\"customer-form\"]/div[3]/div[2]/div/button/span[1]")
        self.dr.click("xpath->//*[@id=\"customer-form\"]/div[3]/div[2]/div/div/ul/li[2]/a")
        phoneno= '13' +str(random.randrange(4,10))+''.join( str(random.choice(range(10))) for i in range(8))
        self.dr.type("id->customer-mobile",phoneno)
        self.dr.type("xpath->//*[@id=\"enterprise-enterprise_name\"]",'企业2')
        self.dr.wait(3)
        sleep(2)
        self.dr.click("css->#btn-add-customer")
        self.dr.wait(3)
        self.dr.switch_to_frame_out()
        sleep(2)
        self.dr.click("link_text->客户资料")
        self.dr.switch_to_frame("id->iframe_standard_crm_customer_index")
        self.dr.click("xpath->//*[@id=\"customer-search-form\"]/div[12]/button")
        self.dr.wait(3)
        sleep(2)
        #tables = self.dr.origin_driver.find_element_by_xpath("//*[@id=\"customer-grid\"]/div[1]/table")
        #rows2 = len(tables.find_elements_by_tag_name('tr'))
        db = pymysql.connect(globalparam.db_standard["ip"], globalparam.db_standard["loginname"],globalparam.db_standard["password"], globalparam.db_standard["basename"], charset='utf8')
        cursor = db.cursor()
        count = cursor.execute("select * from crm_customer where customer_name = '客户2'")
        db.close()
        self.dr.take_screenshot(os.path.join(globalparam.img_path, "customer", "add_customer.png"))
        return count








