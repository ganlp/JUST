import sys
sys.path.append('../..')
from public.common.basepage import Page
from time import sleep
from selenium.webdriver.common.keys import Keys
from config import globalparam
import os
from BeautifulReport import BeautifulReport

class DimissionPage(Page):
    @BeautifulReport.add_test_img('dimission', 'del_dimission')
    def delete_dimission(self):
        self.dr.click("link_text->组织机构")
        self.dr.wait(1)
        self.dr.click("link_text->离职库")
        self.dr.switch_to_frame("id->iframe_organize_user_level")
        cnt1=int(self.dr.get_text("xpath->//*[@id=\"user-grid\"]/div[2]/div/div[1]/div[1]").strip("条")[1:])
        self.dr.click("xpath->//*[@id=\"user-grid\"]/div[1]/table/tbody/tr[1]/td[9]/a[2]")
        self.dr.switch_to_frame_out()
        self.dr.click("css->body > div.ui-popup.ui-popup-modal.ui-popup-show.ui-popup-focus > div > table > tbody > tr:nth-child(3) > td > div.ui-dialog-button > button.ui-dialog-autofocus")
        self.dr.switch_to_frame("id->iframe_organize_user_level")
        cnt2 = int(self.dr.get_text("xpath->//*[@id=\"user-grid\"]/div[2]/div/div[1]/div[1]").strip("条")[1:])
        self.dr.take_screenshot(os.path.join(globalparam.img_path, "dimission", "del_dimission.png"))
        return (cnt1,cnt2)

    @BeautifulReport.add_test_img('dimission', 'recover_dimission')
    def recover_dimission(self):
        self.dr.click("link_text->组织机构")
        self.dr.wait(1)
        self.dr.click("link_text->离职库")
        self.dr.switch_to_frame("id->iframe_organize_user_level")
        cnt1 = int(self.dr.get_text("xpath->//*[@id=\"user-grid\"]/div[2]/div/div[1]/div[1]").strip("条")[1:])
        self.dr.click("xpath->//*[@id=\"user-grid\"]/div[1]/table/tbody/tr[1]/td[9]/a[1]")
        sleep(2)
        cnt2 = int(self.dr.get_text("xpath->//*[@id=\"user-grid\"]/div[2]/div/div[1]/div[1]").strip("条")[1:])
        self.dr.take_screenshot(os.path.join(globalparam.img_path, "dimission", "recover_dimission.png"))
        return (cnt1, cnt2)