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
        #self.dr = pyselenium.PySelenium(globalparam.browser,'127.0.0.1:8080')
        self.dr = pyselenium.PySelenium(globalparam.browser)
        self.dr.open(globalparam.server_addr)
        self.dr.wait(5)
        sleep(2)
        self.dr.max_window()
        self.dr.wait(10)

    def login_with_cookie(self):
        with open(globalparam.cookie_path_userweb,'r') as f:
            cookie = f.read()
     #   self.dr.origin_driver.delete_all_cookies()
        cookie=eval(cookie)
        for c in cookie:
            self.dr.origin_driver.add_cookie(c)
        self.dr.origin_driver.refresh()
        self.dr.wait(10)

    def tearDown(self):
        self.dr.quit()
        self.logger.info('###############################  End  ###############################')
