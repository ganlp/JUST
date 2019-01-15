import sys
sys.path.append('../..')
from public.common.basepage import Page
from time import sleep
from selenium.webdriver.common.keys import Keys
from config import globalparam
import os
from BeautifulReport import BeautifulReport

class DepartPage(Page):
    @BeautifulReport.add_test_img('depart', 'add_depart')
    def add_depart(self):
     #   self.dr.click("xpath->//*[@id=\"sidebar\"]/ul/li/div/a[12]/span")
     #   self.dr.click("css->#sidebar > ul > li > div > a:nth-child(15) > span")
        self.dr.click("link_text->组织机构")
        self.dr.wait(1)
        self.dr.click("link_text->部门管理")
        self.dr.switch_to_frame("id->iframe_organize_department")
        sleep(2)
        tables=self.dr.origin_driver.find_element_by_xpath("//*[@id=\"w0\"]/div[1]/table")
        rows1=len(tables.find_elements_by_tag_name('tr'))
        self.dr.click("link_text->新建")
        self.dr.switch_to_frame_out()
        self.dr.switch_to_frame("id->iframe_organize_department_POP")
        self.dr.wait(5)
        sleep(1)
        self.dr.type("css->#department-dept_name",'测试部1')
        self.dr.click("xpath->//*[@id=\"department-form\"]/div[6]/button")
        self.dr.wait(5)
        self.dr.switch_to_frame_out()
        self.dr.switch_to_frame("id->iframe_organize_department")
        sleep(5)
        tables=self.dr.origin_driver.find_element_by_xpath("//*[@id=\"w0\"]/div[1]/table")
        self.dr.take_screenshot(os.path.join(globalparam.img_path,"depart","add_depart.png"))
        rows2=len(tables.find_elements_by_tag_name('tr'))
        return [rows1,rows2]

    @BeautifulReport.add_test_img('depart', 'del_depart')
    def del_depart(self):
       # self.dr.click("css->#sidebar > ul > li > div > a:nth-child(15) > span")
        self.dr.click("link_text->组织机构")
        self.dr.wait(1)
        self.dr.click("link_text->部门管理")
        self.dr.switch_to_frame("id->iframe_organize_department")
        sleep(2)
        tables=self.dr.origin_driver.find_element_by_xpath("//*[@id=\"w0\"]/div[1]/table")
        self.dr.wait(5)
        rows1=tables.find_elements_by_tag_name("tr")
        rows1[-1].find_element_by_link_text("删除").click()
        self.dr.switch_to_frame_out()
        self.dr.wait(5)
        sleep(2)
        self.dr.click("css->body > div.ui-popup.ui-popup-modal.ui-popup-show.ui-popup-focus > div > table > tbody > tr:nth-child(3) > td > div.ui-dialog-button > button.ui-dialog-autofocus")
 #       self.dr.click("xpath->/html/body/div[10]/div/table/tbody/tr[3]/td/div[2]/button[2]")
        self.dr.wait(5)
        self.dr.switch_to_frame("id->iframe_organize_department")
        sleep(5)
        tables=self.dr.origin_driver.find_element_by_xpath("//*[@id=\"w0\"]/div[1]/table")
        self.dr.take_screenshot(os.path.join(globalparam.img_path,"depart","del_depart.png"))
        rows2=tables.find_elements_by_tag_name("tr")
    #    self.dr.switch_to_frame_out()
        return  [len(rows1),len(rows2)]




