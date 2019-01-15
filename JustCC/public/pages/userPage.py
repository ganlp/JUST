__author__ = 'ganlp'

import sys
sys.path.append('../..')
from public.common.basepage import Page
from time import sleep
import os
from config import globalparam
from BeautifulReport import BeautifulReport

class UserPage(Page):
    @BeautifulReport.add_test_img('user', 'add_user')
    def add_user(self,work_no,work_name,username):
        #self.dr.click("css->#sidebar > ul > li > div > a:nth-child(15) > span")
        self.dr.click("link_text->组织机构")
        self.dr.wait(1)
        self.dr.click("link_text->用户管理")
        self.dr.wait(5)
        self.dr.switch_to_frame("id->iframe_organize_user")
        sleep(2)
        tables=self.dr.origin_driver.find_element_by_xpath("//*[@id=\"user-grid\"]/div[1]/table")
        rows1=tables.find_elements_by_tag_name("tr")
        self.dr.click("css->#user-add")  #点击新建按钮
        sleep(2)
        self.dr.switch_to_frame_out()
        self.dr.wait(5)
        self.dr.switch_to_frame("id->iframe_organize_user_POP")
        self.dr.wait(3)
        self.dr.type("xpath->//*[@id=\"user-agent_number\"]",work_no)
        self.dr.type("css->#user-username",work_name)
        self.dr.type("css->#user-realname",username)
        self.dr.click("xpath->//*[@id=\"user-form\"]/div[6]/div[2]/div/div/button/span[1]")
        sleep(1)
        self.dr.click("xpath->//*[@id=\"user-form\"]/div[6]/div[2]/div/div/div/ul/li[2]/a")
        self.dr.click("xpath->//*[@id=\"user-form\"]/div[7]/div[2]/div/div/button/span[1]")
        sleep(1)
        self.dr.click("xpath->//*[@id=\"user-form\"]/div[7]/div[2]/div/div/div/ul/li[2]/a/span[1]")
        self.dr.clear_type("css->#user-password",'Aa111111')
        self.dr.clear_type("css->#user-confirm_password",'Aa111111')
        self.dr.click("css->#user-form > div.btn_box > button")
        self.dr.wait(5)
        self.dr.switch_to_frame_out()
        self.dr.switch_to_frame("id->iframe_organize_user")
        sleep(2)
        tables=self.dr.origin_driver.find_element_by_xpath("//*[@id=\"user-grid\"]/div[1]/table")
        rows2=tables.find_elements_by_tag_name("tr")
        self.dr.switch_to_frame_out()
        sleep(3)
        self.dr.take_screenshot(os.path.join(globalparam.img_path,"user","add_user.png"))
        return  [len(rows1),len(rows2)]

    @BeautifulReport.add_test_img('user', 'del_user')
    def del_user(self,n):
        #self.dr.click("css->#sidebar > ul > li > div > a:nth-child(15) > span")
        self.dr.click("link_text->组织机构")
        self.dr.wait(1)
        self.dr.click("link_text->用户管理")
        self.dr.wait(5)
        self.dr.switch_to_frame("id->iframe_organize_user")
        sleep(2)
        for i in range(n):
            tables=self.dr.origin_driver.find_element_by_xpath("//*[@id=\"user-grid\"]/div[1]/table")
            rows1=tables.find_elements_by_tag_name("tr")
            sleep(2)
            rows1[1].find_element_by_link_text("离职").click()
            self.dr.switch_to_frame_out()
            self.dr.wait(5)
            sleep(2)
            self.dr.click("css->body > div.ui-popup.ui-popup-modal.ui-popup-show.ui-popup-focus > div > table > tbody > tr:nth-child(3) > td > div.ui-dialog-button > button.ui-dialog-autofocus")
            self.dr.switch_to_frame("id->iframe_organize_user")
            self.dr.wait(20)
            sleep(3)
        tables=self.dr.origin_driver.find_element_by_xpath("//*[@id=\"user-grid\"]/div[1]/table")
        self.dr.take_screenshot(os.path.join(globalparam.img_path,"user","del_user.png"))
        rows2=tables.find_elements_by_tag_name("tr")
        return  [len(rows1),len(rows2)]







