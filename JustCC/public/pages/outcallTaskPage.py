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
        self.dr.type("xpath->//*[@id=\"object-object_name\"]","测试预览式")
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

    @BeautifulReport.add_test_img('manualoutcall', 'import_number')
    def import_number(self):
        self.dr.click("link_text->人工外呼")
        self.dr.wait(1)
        self.dr.click("link_text->项目管理")
        self.dr.switch_to_frame("id->iframe_outbound_object_index")
        self.dr.click("xpath->//*[@id=\"w0\"]/div[1]/table/tbody/tr[1]/td[8]/div/a[4]")
        self.dr.switch_to_frame_out()
        self.dr.click("xpath->//*[@id=\"content:pop\"]/div/p[2]/a[1]")
        self.dr.switch_to_frame("id->pop")
        self.dr.click("xpath->//*[@id=\"customer-grid\"]/div[1]/table/tbody/tr[1]/td[1]/label/i")
        self.dr.click("xpath->//*[@id=\"customer-import\"]")
        self.dr.take_screenshot(os.path.join(globalparam.img_path, "manualoutcall", "import_number.png"))
        sleep(2)
        
    @BeautifulReport.add_test_img('manualoutcall', 'task_unable')
    def task_unable(self):
        self.dr.click("link_text->人工外呼")
        self.dr.wait(1)
        self.dr.click("link_text->项目管理")
        self.dr.switch_to_frame("id->iframe_outbound_object_index")
        self.dr.click("xpath->//*[@id=\"w0\"]/div[1]/table/tbody/tr[1]/td[8]/div/a[1]")
        self.dr.switch_to_frame_out()
        self.dr.click("xpath->/html/body/div[9]/div/table/tbody/tr[3]/td/div[2]/button[2]")
        sleep(3)
        self.dr.switch_to_frame("id->iframe_outbound_object_index")
        status=self.dr.get_text("xpath->//*[@id=\"w0\"]/div[1]/table/tbody/tr[1]/td[8]/div/a[1]")
        self.dr.take_screenshot(os.path.join(globalparam.img_path, "manualoutcall", "task_unable.png"))
        return status

    @BeautifulReport.add_test_img('manualoutcall', 'task_enable')
    def task_enable(self):
        self.dr.click("link_text->人工外呼")
        self.dr.wait(1)
        self.dr.click("link_text->项目管理")
        self.dr.switch_to_frame("id->iframe_outbound_object_index")
        self.dr.click("xpath->//*[@id=\"w0\"]/div[1]/table/tbody/tr[1]/td[8]/div/a[1]")
        self.dr.switch_to_frame_out()
        self.dr.click("xpath->/html/body/div[9]/div/table/tbody/tr[3]/td/div[2]/button[2]")
        sleep(3)
        self.dr.switch_to_frame("id->iframe_outbound_object_index")
        status = self.dr.get_text("xpath->//*[@id=\"w0\"]/div[1]/table/tbody/tr[1]/td[8]/div/a[1]")
        self.dr.take_screenshot(os.path.join(globalparam.img_path, "manualoutcall", "task_enable.png"))
        return status

    @BeautifulReport.add_test_img('manualoutcall', 'task_del')
    def task_del(self):
        self.dr.click("link_text->人工外呼")
        self.dr.wait(1)
        self.dr.click("link_text->项目管理")
        self.dr.switch_to_frame("id->iframe_outbound_object_index")
        cnt1 = int(self.dr.get_text("xpath->//*[@id=\"w0\"]/div[2]/div/div[1]/div[1]").strip("条")[1:])
        self.dr.click("xpath->//*[@id=\"w0\"]/div[1]/table/tbody/tr[1]/td[8]/div/a[3]")
        self.dr.switch_to_frame_out()
        sleep(1)
        self.dr.click("css->.ui-dialog-autofocus")
        sleep(2)
        self.dr.switch_to_frame("id->iframe_outbound_object_index")
        cnt2 = int(self.dr.get_text("xpath->//*[@id=\"w0\"]/div[2]/div/div[1]/div[1]").strip("条")[1:])
        self.dr.take_screenshot(os.path.join(globalparam.img_path, "manualoutcall", "task_del.png"))
        return [cnt1,cnt2]
