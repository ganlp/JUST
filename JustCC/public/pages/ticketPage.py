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

class TicketPage(Page):
    @BeautifulReport.add_test_img('ticket','add_ticket_type')
    def add_ticket_type(self):  #新建工单类型
      self.dr.click("link_text->系统设置")
      self.dr.wait(1)
      self.dr.click("link_text->字段设置")
      self.dr.wait(1)
      self.dr.click("link_text->工单字段")
      self.dr.wait(1)
      self.dr.switch_to_frame("id->iframe_standard_system_field_index_ticket")
      self.dr.click("css->body > div > div > div > div.sub_left_menu > ul > li:nth-child(2) > a")
      self.dr.wait(1)
      self.dr.click("xpath->//*[@id=\"ticket-type-add\"]")
      self.dr.switch_to_frame_out()
      self.dr.switch_to_frame("id->create-ticket-type")
      self.dr.type("xpath->//*[@id=\"tickettype-type_name\"]","请假")
      self.dr.click("xpath->//*[@id=\"ticket-type-form\"]/div[3]/div/button")
      self.dr.switch_to_frame_out()
      self.dr.switch_to_frame("id->iframe_standard_system_field_index_ticket")
      self.dr.wait(2)
      sleep(2)
      db = pymysql.connect(globalparam.db_standard["ip"], globalparam.db_standard["loginname"],
                           globalparam.db_standard["password"], globalparam.db_standard["basename"], charset='utf8')
      cursor = db.cursor()
      count = cursor.execute("select * from conf_ticket_type where type_name = '请假'")
      db.close()
      self.dr.take_screenshot(os.path.join(globalparam.img_path, "ticket", "add_ticket_type.png"))
      return count

    @BeautifulReport.add_test_img('ticket', 'add_ticket_new')
    def add_ticket_new(self): #创建新建状态工单
     #   self.dr.click("xpath->//*[@id=\"sidebar\"]/ul/li/div/a[12]/span")
     #   self.dr.click("css->#sidebar > ul > li > div > a:nth-child(15) > span")
        self.dr.click("link_text->工单管理")
        self.dr.wait(3)
        self.dr.click("link_text->创建工单")
        self.dr.wait(3)
        self.dr.switch_to_frame("id->iframe_ticket-create")
        self.dr.click("xpath->//*[@id=\"create_ticket_main\"]/table/tbody/tr/td/div/button/span[2]/span")
        self.dr.wait(3)
        self.dr.click("xpath->//*[@id=\"create_ticket_main\"]/table/tbody/tr/td/div/div/ul/li[2]/a")
        self.dr.wait(3)
        self.dr.click("xpath->//*[@id=\"create_ticket_main\"]/table/tbody/tr[11]/td/div/button")
        self.dr.click("xpath->//*[@id=\"create_ticket_main\"]/table/tbody/tr[11]/td/div/div/ul/li[2]/a")
        self.dr.type("xpath->//*[@id=\"ticketmain-title\"]","请假3天")
        self.dr.type("xpath->//*[@id=\"ticketmain-content\"]","请假回家过年")
        self.dr.wait(2)
        self.dr.click("xpath->//*[@id=\"save_ticket_main\"]")
        self.dr.wait(2)
        sleep(2)
        db = pymysql.connect(globalparam.db_standard["ip"], globalparam.db_standard["loginname"],
                         globalparam.db_standard["password"], globalparam.db_standard["basename"], charset='utf8')
        cursor = db.cursor()
        count = cursor.execute("select * from ticket_main where title = '请假3天'")
        db.close()
        self.dr.take_screenshot(os.path.join(globalparam.img_path,"ticket", "add_ticket_new.png"))
        return count

    @BeautifulReport.add_test_img('ticket', 'add_ticket_finish')
    def add_ticket_finish(self):  # 创建完结工单
        #   self.dr.click("xpath->//*[@id=\"sidebar\"]/ul/li/div/a[12]/span")
        #   self.dr.click("css->#sidebar > ul > li > div > a:nth-child(15) > span")
        self.dr.click("link_text->工单管理")
        self.dr.wait(3)
        self.dr.click("link_text->创建工单")
        self.dr.wait(3)
        self.dr.switch_to_frame("id->iframe_ticket-create")
        self.dr.click("xpath->//*[@id=\"create_ticket_main\"]/table/tbody/tr/td/div/button/span[2]/span")
        self.dr.wait(3)
        self.dr.click("xpath->//*[@id=\"create_ticket_main\"]/table/tbody/tr/td/div/div/ul/li[2]/a")
        self.dr.wait(3)
        self.dr.click("xpath->//*[@id=\"create_ticket_main\"]/table/tbody/tr[3]/td/div/button/span[1]")
        self.dr.click("xpath->//*[@id=\"create_ticket_main\"]/table/tbody/tr[3]/td/div/div/ul/li[4]/a")
        self.dr.click("xpath->//*[@id=\"create_ticket_main\"]/table/tbody/tr[11]/td/div/button")
        self.dr.click("xpath->//*[@id=\"create_ticket_main\"]/table/tbody/tr[11]/td/div/div/ul/li[2]/a")
        self.dr.type("xpath->//*[@id=\"ticketmain-title\"]", "请假1天")
        self.dr.type("xpath->//*[@id=\"ticketmain-content\"]", "病假")
        self.dr.wait(2)
        self.dr.click("xpath->//*[@id=\"save_ticket_main\"]")
        self.dr.wait(2)
        sleep(2)
        db = pymysql.connect(globalparam.db_standard["ip"], globalparam.db_standard["loginname"],
                             globalparam.db_standard["password"], globalparam.db_standard["basename"], charset='utf8')
        cursor = db.cursor()
        count = cursor.execute("select * from ticket_main where title = '请假1天'")
        db.close()
        self.dr.take_screenshot(os.path.join(globalparam.img_path, "ticket", "add_ticket_finish.png"))
        return count

    @BeautifulReport.add_test_img('ticket', 'add_ticket_attachment')
    def add_ticket_attachment(self):  # 创建新建工单带附件
        #   self.dr.click("xpath->//*[@id=\"sidebar\"]/ul/li/div/a[12]/span")
        #   self.dr.click("css->#sidebar > ul > li > div > a:nth-child(15) > span")
        self.dr.click("link_text->工单管理")
        self.dr.wait(3)
        self.dr.click("link_text->创建工单")
        self.dr.wait(3)
        self.dr.switch_to_frame("id->iframe_ticket-create")
        self.dr.click("xpath->//*[@id=\"create_ticket_main\"]/table/tbody/tr/td/div/button/span[2]/span")
        self.dr.wait(3)
        self.dr.click("xpath->//*[@id=\"create_ticket_main\"]/table/tbody/tr/td/div/div/ul/li[2]/a")
        self.dr.wait(3)
        self.dr.click("xpath->//*[@id=\"create_ticket_main\"]/table/tbody/tr[11]/td/div/button")
        self.dr.click("xpath->//*[@id=\"create_ticket_main\"]/table/tbody/tr[11]/td/div/div/ul/li[2]/a")
        self.dr.type("xpath->//*[@id=\"ticketmain-title\"]", "请假1天带jpg附件")
        self.dr.type("xpath->//*[@id=\"ticketmain-content\"]", "病假附件有图片")
        self.dr.wait(2)
        self.dr.type("xpath->//*[@id=\"upload_file\"]","F:\\attachment.jpg")
        self.dr.wait(2)
        self.dr.click("xpath->//*[@id=\"save_ticket_main\"]")
        self.dr.wait(2)
        sleep(2)
        db = pymysql.connect(globalparam.db_standard["ip"], globalparam.db_standard["loginname"],
                             globalparam.db_standard["password"], globalparam.db_standard["basename"], charset='utf8')
        cursor = db.cursor()
        count = cursor.execute("select * from ticket_main where title = '请假1天带jpg附件'")
        db.close()
        self.dr.take_screenshot(os.path.join(globalparam.img_path, "ticket", "add_ticket_attachment.png"))
        return count




