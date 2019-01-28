import sys
sys.path.append('../..')
from public.pages import loginPage
from config import globalparam
from public.common import pyselenium
from time import sleep

class Login():
    def login(self):
        self.dr1 = pyselenium.PySelenium(globalparam.browser)
        self.dr1.open(globalparam.server_addr)
        self.dr1.wait(10)
        sleep(2)
        self.dr1.max_window()
        self.login_page=loginPage.LoginPage(self.dr1)
        self.login_page.static_login('1112','Aa111111')
        sleep(2)
        self.cookies=self.dr1.origin_driver.get_cookies()
        with open(globalparam.cookie_path_userweb,'w') as f:
             f.write(str(self.cookies))

    def login_admin(self):
        self.dr2 = pyselenium.PySelenium(globalparam.browser)
        self.dr2.open(globalparam.server_addr+"/admin")
        self.dr2.wait(10)
        self.dr2.max_window()
        self.login_page = loginPage.LoginPage(self.dr2)
        self.login_page.admin_login('admin', 'justpass')
        sleep(2)
        try:
            self.dr2.accept_alert()
        except:
            pass
        self.cookies = self.dr2.origin_driver.get_cookies()
        with open(globalparam.cookie_path_admin, 'w') as f:
            f.write(str(self.cookies))

if __name__=='__main__':
    lg=Login()
    lg.login()
    lg.login_admin()