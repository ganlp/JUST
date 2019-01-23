import sys
sys.path.append('../..')
from public.common.basepage import Page
from time import sleep
from selenium.webdriver.common.keys import Keys
from config import globalparam
import os
import random
import pymysql
from BeautifulReport import BeautifulReport

class CustomerPage(Page):
    @BeautifulReport.add_test_img('customer', 'add_customer')
    def add_customer(self):
     #   self.dr.click("xpath->//*[@id=\"sidebar\"]/ul/li/div/a[12]/span")
     #   self.dr.click("css->#sidebar > ul > li > div > a:nth-child(15) > span")
        self.dr.click("link_text->客户管理")
        self.dr.click("link_text->客户资料")
        self.dr.switch_to_frame("id->iframe_standard_crm_customer_index")
        #tables=self.dr.origin_driver.find_element_by_xpath("//*[@id=\"customer-grid\"]/div[1]/table")
        #rows1 = len(tables.find_elements_by_tag_name('tr'))
        self.dr.click("xpath->/html/body/div/header/div[2]/a")
        self.dr.switch_to_frame_out()
        self.dr.switch_to_frame("id->iframe_standard_crm_customer_create")
        self.dr.type("xpath->//*[@id=\"customer-customer_name\"]","客户2")
        self.dr.click("xpath->//*[@id=\"customer-form\"]/div[3]/div[2]/div/button/span[1]")
        self.dr.click("xpath->//*[@id=\"customer-form\"]/div[3]/div[2]/div/div/ul/li[2]/a")
        phoneno= '13' +str(random.randrange(4,10))+''.join( str(random.choice(range(10))) for i in range(8))
        self.dr.type("id->customer-mobile",phoneno)
        self.dr.type("xpath->//*[@id=\"enterprise-enterprise_name\"]",'企业2')
        self.dr.click("css->#btn-add-customer")
        self.dr.switch_to_frame_out()
        self.dr.click("link_text->客户资料")
        self.dr.switch_to_frame("id->iframe_standard_crm_customer_index")
        self.dr.click("css->#customer-search-form > div:nth-child(13) > button")
        sleep(1)
        #tables = self.dr.origin_driver.find_element_by_xpath("//*[@id=\"customer-grid\"]/div[1]/table")
        #rows2 = len(tables.find_elements_by_tag_name('tr'))
        db = pymysql.connect(globalparam.db_standard["ip"], globalparam.db_standard["loginname"],globalparam.db_standard["password"], globalparam.db_standard["basename"], charset='utf8')
        cursor = db.cursor()
        count = cursor.execute("select * from crm_customer where customer_name = '客户2'")
        db.close()
        self.dr.take_screenshot(os.path.join(globalparam.img_path, "customer", "add_customer.png"))
        return count

    @BeautifulReport.add_test_img('customer', 'modify_customer')
    def modify_customer(self): #修改客户资料-设置为私有
       self.dr.click("link_text->客户管理")
       self.dr.wait(1)
       self.dr.click("link_text->客户资料")
       self.dr.switch_to_frame("id->iframe_standard_crm_customer_index")
       customer_id=self.dr.get_text("xpath->//*[@id=\"customer-grid\"]/div[1]/table/tbody/tr[1]/td[2]")
       self.dr.click("xpath->//*[@id=\"customer-grid\"]/div[1]/table/tbody/tr[1]/td[3]")
       self.dr.switch_to_frame_out()
       frame_id="iframe_standard_crm_customer_update_"+customer_id
       self.dr.switch_to_frame("id->"+frame_id)
       self.dr.click("xpath->//*[@id=\"customer-belong\"]/label[2]")
       self.dr.click("xpath->//*[@id=\"btn-add-customer\"]")
       self.dr.switch_to_frame_out()
       self.dr.click("link_text->客户资料")
       self.dr.switch_to_frame("id->iframe_standard_crm_customer_index")
       self.dr.click("css->#customer-search-form > div:nth-child(13) > button")
       is_private=self.dr.get_text("xpath->//*[@id=\"customer-grid\"]/div[1]/table/tbody/tr[1]/td[6]")
       self.dr.take_screenshot(os.path.join(globalparam.img_path, "customer", "modify_customer.png"))
       return is_private

    @BeautifulReport.add_test_img('customer', 'del_customer')
    def del_customer(self):  # 删除客户资料
       self.dr.click("link_text->客户管理")
       self.dr.wait(1)
       self.dr.click("link_text->客户资料")
       self.dr.switch_to_frame("id->iframe_standard_crm_customer_index")
       cnt1=int(self.dr.get_text("xpath->//*[@id=\"customer-grid\"]/div[2]/div/div[1]/div[1]").strip("条")[1:])
       self.dr.click("xpath->//*[@id=\"customer-grid\"]/div[1]/table/tbody/tr[1]/td[1]/label/i")
       self.dr.click("xpath->//*[@id=\"btn-customer-delete\"]")
       self.dr.switch_to_frame_out()
       self.dr.click("xpath->/html/body/div[9]/div/table/tbody/tr[3]/td/div[2]/button[2]")
       self.dr.switch_to_frame("id->iframe_standard_crm_customer_index")
       cnt2=int(self.dr.get_text("xpath->//*[@id=\"customer-grid\"]/div[2]/div/div[1]/div[1]").strip("条")[1:])
       self.dr.take_screenshot(os.path.join(globalparam.img_path, "customer", "del_customer.png"))
       return [cnt1,cnt2]

    @BeautifulReport.add_test_img('customer', 'del_customer_from_recycle')
    def del_customer_from_recycle(self):  #从回收站删除
       self.dr.click("link_text->客户管理")
       self.dr.wait(1)
       self.dr.click("link_text->回收站")
       self.dr.switch_to_frame("id->iframe_standard_customer_recycle")
       cnt1 = int(self.dr.get_text("xpath->//*[@id=\"recycle-grid\"]/div[2]/div/div[1]/div[1]").strip("条")[1:])
       self.dr.click("xpath->//*[@id=\"recycle-grid\"]/div[1]/table/tbody/tr/td[1]/label/i")
       self.dr.click("xpath->//*[@id=\"btn-select-delete\"]")
       self.dr.switch_to_frame_out()
       self.dr.click("css->body > div.ui-popup.ui-popup-modal.ui-popup-show.ui-popup-focus > div > table > tbody > tr:nth-child(3) > td > div.ui-dialog-button > button.ui-dialog-autofocus")
       self.dr.switch_to_frame("id->iframe_standard_customer_recycle")
       sleep(1)
       cnt2=int(self.dr.get_text("xpath->//*[@id=\"recycle-grid\"]/div[2]/div/div[1]/div[1]").strip("条")[1:])
       self.dr.take_screenshot(os.path.join(globalparam.img_path, "customer", "del_customer_from_recycle.png"))
       return [cnt1, cnt2]





