import sys
sys.path.append('../..')
from public.common.basepage import Page
from time import sleep
from config import globalparam
import os
from BeautifulReport import BeautifulReport

class OutcallclassifyPage(Page):
    @BeautifulReport.add_test_img('manualoutcall', 'add_classify')
    def add_classify(self):
        self.dr.click("link_text->人工外呼")
        self.dr.wait(1)
        self.dr.click("link_text->电销分类")
        self.dr.switch_to_frame("id->iframe_outbound_task_category_index")
        cnt1=int(self.dr.get_text("xpath->//*[@id=\"outbound-task-category\"]/div[2]/div/div[1]/div[1]").strip("条")[1:])
        self.dr.click("xpath->//*[@id=\"addType\"]")
        self.dr.switch_to_frame_out()
        self.dr.type("xpath->//*[@id=\"taskcategory-name\"]","测试分类")
        self.dr.click("xpath->//*[@id=\"outbound-task-category\"]/div[2]/button[2]")
        self.dr.switch_to_frame("id->iframe_outbound_task_category_index")
        cnt2 = int(self.dr.get_text("xpath->//*[@id=\"outbound-task-category\"]/div[2]/div/div[1]/div[1]").strip("条")[1:])
        self.dr.take_screenshot(os.path.join(globalparam.img_path, "manualoutcall", "add_classify.png"))
        return (cnt1,cnt2)

    @BeautifulReport.add_test_img('manualoutcall', 'classify_disable')
    def classify_disable(self):
        self.dr.click("link_text->人工外呼")
        self.dr.wait(1)
        self.dr.click("link_text->电销分类")
        self.dr.switch_to_frame("id->iframe_outbound_task_category_index")
        self.dr.click("xpath->//*[@id=\"outbound-task-category\"]/div[1]/table/tbody/tr[1]/td[3]/a[3]")
        sleep(2)
        status=self.dr.get_text("xpath->//*[@id=\"outbound-task-category\"]/div[1]/table/tbody/tr[1]/td[2]/span")
        self.dr.take_screenshot(os.path.join(globalparam.img_path, "manualoutcall", "classify_disable.png"))
        return status

