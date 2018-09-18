__author__ = 'ganlp'

import sys
sys.path.append('../..')
from public.common.basepage import Page
from config import globalparam
from time import sleep
import os


class LoginPage(Page):
    def static_login(self,username,password):
        self.dr.wait(5)
        self.dr.clear_type('name->LoginForm[username]',username)
        self.dr.clear_type('name->LoginForm[password]',password)
        self.dr.click('id->login_btn')
        self.dr.wait(20)
      #  self.cookies=self.dr.origin_driver.get_cookies()
        sleep(10)
        self.dr.take_screenshot(os.path.join(globalparam.img_path,"login","login.png"))

    def admin_login(self,username,password):
        self.dr.wait(5)
        self.dr.clear_type('name->username',username)
        self.dr.clear_type('name->password',password)
        self.dr.click('css->#loginform > div:nth-child(4) > button')
    #    self.cookies = self.dr.origin_driver.get_cookies()

    def return_title(self):
        """返回该页面的title"""
        return self.dr.get_title()

    def logout(self):
        self.dr.click("id->logout")
        sleep(10)
        self.dr.click("xpath->/html/body/div[5]/div/table/tbody/tr[3]/td/div[2]/button[2]")
        sleep(5)


