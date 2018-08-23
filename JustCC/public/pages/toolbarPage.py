__author__ = 'Administrator'
'''
右上角工具条
'''
import sys
sys.path.append('../..')
from public.common.basepage import Page
from time import sleep
from selenium.webdriver.common.keys import Keys
from config import globalparam
import os

class ToolbarPage(Page):
    def quick_call(self):
        self.dr.type("xpath->//*[@id=\"top_search\"]","13421344506")
        self.dr.wait(5)
        self.dr.js_click(".makeCall")
        sleep(3)
        self.dr.take_screenshot(os.path.join(globalparam.img_path,"toolbar","login.png"))
        pass
