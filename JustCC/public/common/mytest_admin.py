  #coding=utf-8

import unittest
import sys
sys.path.append('../..')
from public.common import pyselenium
from config import globalparam
from public.common.log import Log
from time import sleep

class MyTest(unittest.TestCase):
    """
    The base class is for all testcase.
    """
    def setUp(self):
        self.logger = Log()
        self.logger.info('############################### START ###############################')
        self.dr = pyselenium.PySelenium(globalparam.browser)
        self.dr.open(globalparam.server_addr+"/admin")
        self.dr.wait(10)
        sleep(2)
        self.dr.max_window()

    def login_admin_with_cookie(self):
        with open(globalparam.cookie_path_admin,'r') as f:
            cookie = f.read()
        self.dr.origin_driver.delete_all_cookies()
        cookie = eval(cookie)
        for c in cookie:
            self.dr.origin_driver.add_cookie(c)
        self.dr.origin_driver.refresh()
        self.dr.wait(10)
        self.dr.accept_alert()

    def tearDown(self):
        self.dr.quit()
        self.logger.info('###############################  End  ###############################')

