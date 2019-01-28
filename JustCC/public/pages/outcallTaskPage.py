import sys
sys.path.append('../..')
from public.common.basepage import Page
from time import sleep
from config import globalparam
import os
from BeautifulReport import BeautifulReport

class OutcallTaskPage(Page):
    @BeautifulReport.add_test_img('manualoutcall', 'add_task')
    def add_task(self):
        self.dr.click("link_text->人工外呼")
        self.dr.wait(1)
        self.dr.click("link_text->项目管理")
        self.dr.switch_to_frame("id->iframe_outbound_object_index")
        cnt1 = int(self.dr.get_text("xpath->//*[@id=\"w0\"]/div[2]/div/div[1]/div[1]").strip("条")[1:])
        self.dr.click("xpath->//*[@id=\"user-add\"]")
        self.dr.switch_to_frame_out()
        self.dr.switch_to_frame("id->iframe_outbound_object_create")
        self.dr.type("xpath->//*[@id=\"object-object_name\"]","预览式")
        self.dr.click("xpath->//*[@id=\"object-form\"]/div[11]/div[2]/div/div/button/span[1]")
        self.dr.click("xpath->//*[@id=\"object-form\"]/div[11]/div[2]/div/div/div/ul/li[2]/a/span[1]")
        sleep(1)
        self.dr.click("css->.show_select_data.work_user_box")
        self.dr.switch_to_frame_out()
        self.dr.switch_to_frame("id->iframeLabel")
        self.dr.click("xpath->//*[@id=\"dept_tree\"]/ul/li/div/span")
        self.dr.type("xpath->//*[@id=\"searchInput\"]","甘")
        self.dr.click("xpath->//*[@id=\"search\"]")
        self.dr.click("xpath->//*[@id=\"result_box_ul\"]/li[2]/div/label/i")
        self.dr.click("xpath->//*[@id=\"saveRole\"]")
        self.dr.switch_to_frame_out()
        self.dr.switch_to_frame("id->iframe_outbound_object_create")
        self.dr.click("xpath->//*[@id=\"object-form\"]/div[20]/button")
        sleep(2)
        self.dr.switch_to_frame_out()
        self.dr.click("link_text->项目管理")
        self.dr.switch_to_frame("id->iframe_outbound_object_index")
        self.dr.click("xpath->//*[@id=\"btn-search\"]")
        cnt2=int(self.dr.get_text("xpath->//*[@id=\"w0\"]/div[2]/div/div[1]/div[1]").strip("条")[1:])
        self.dr.take_screenshot(os.path.join(globalparam.img_path, "manualoutcall", "add_task.png"))
        return [cnt1,cnt2]