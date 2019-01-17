import sys
sys.path.append('../..')
from public.pages import loginPage
from public.common import datainfo
import json
from config import globalparam
from time import sleep
import unittest
from public.common import pyselenium
from time import sleep

class Login():
    """登录测试"""
    def login(self):
        self.dr = pyselenium.PySelenium(globalparam.browser)
        self.dr.open(globalparam.server_addr)
        self.dr.wait(10)
        sleep(2)
        self.dr.max_window()
        self.login_page=loginPage.LoginPage(self.dr)
        self.login_page.static_login('1112','Aa111111')
        sleep(2)
        self.cookies=self.dr.origin_driver.get_cookies()
        with open(globalparam.cookie_path_userweb,'w') as f:
             f.write(str(self.cookies))

    def login_admin(self):
        self.dr = pyselenium.PySelenium(globalparam.browser)
        self.dr.open(globalparam.server_addr+"/admin")
        self.dr.wait(10)
        self.dr.max_window()
        self.login_page = loginPage.LoginPage(self.dr)
        self.login_page.admin_login('admin', 'justpass')
        sleep(2)
        try:
            self.dr.accept_alert()
        except:
            pass
        self.cookies = self.dr.origin_driver.get_cookies()
        with open(globalparam.cookie_path_admin, 'w') as f:
            f.write(str(self.cookies))

if __name__=='__main__':
    lg=Login()
    lg.login()