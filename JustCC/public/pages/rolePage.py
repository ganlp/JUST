import sys
sys.path.append('../..')
from public.common.basepage import Page
from time import sleep
from selenium.webdriver.common.keys import Keys
from config import globalparam
import os
from BeautifulReport import BeautifulReport

class RolePage(Page):
    @BeautifulReport.add_test_img('role', 'add_role')
    def add_role(self):
        self.dr.click("link_text->组织机构")
        self.dr.wait(1)
        self.dr.click("link_text->角色管理")
        sleep(1)
        self.dr.switch_to_frame("id->iframe_organize_role")
        sleep(10)
        #print(self.dr.get_text("xpath->//*[@id=\"w1\"]/div[2]/div/div[1]/div[1]"))
        cnt1 = int(self.dr.get_text("xpath->//*[@id=\"w1\"]/div[2]/div/div[1]/div[1]").strip("条")[1:])
        self.dr.click("xpath->/html/body/div/header/div[2]/a")
        self.dr.switch_to_frame_out()
        self.dr.switch_to_frame("id->iframe_organize_role_create")
        self.dr.type("xpath->//*[@id=\"role-description\"]","test角色")
        self.dr.click("xpath->//*[@id=\"menuTree_1_check\"]")
        self.dr.click("xpath->//*[@id=\"role-form\"]/div[4]/button")
        sleep(2)
        self.dr.switch_to_frame_out()
        self.dr.click("link_text->角色管理")
        self.dr.switch_to_frame("id->iframe_organize_role")
        self.dr.click("xpath->//*[@id=\"btn-search\"]")
        cnt2=int(self.dr.get_text("xpath->//*[@id=\"w1\"]/div[2]/div/div[1]/div[1]").strip("条")[1:])
        self.dr.take_screenshot(os.path.join(globalparam.img_path, "role", "add_role.png"))
        return [cnt1,cnt2]
    
#// *[ @ id = "w1"] / div[1] / table / tbody / tr[5] / td[3] / a[2]
    @BeautifulReport.add_test_img('role', 'modify_role')
    def add_role(self):
      self.dr.click("link_text->组织机构")
      self.dr.wait(1)
      self.dr.click("link_text->角色管理")
      self.dr.switch_to_frame("id->iframe_organize_role")

