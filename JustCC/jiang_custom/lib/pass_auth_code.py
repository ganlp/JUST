#!/usr/bin/env python
# -*- encoding:utf-8 -*-
# author: jiangtao
import time
from myfunc import Myprint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
myprint=Myprint(34)


class CallScenario(object):
    """页面点击拨号的类、"""
    def __init__(self, ip, port='80'):
        self.ip = ip
        self.login_url = "http://%s:%s/organize/account/login" % (ip, port)
        self.browser = webdriver.Chrome(chrome_options=options)
#        self.browser.maximize_window()
        self.hangup = 'wait'  # 默认为wait、可以设置为send/feedback
        self.menu_sub_list = ['crm', 'ticket', 'outbound',
                              'market', 'monitor', 'standard-quality',
                              'report-calldetails', 'standard-report', 'standard-faq',
                              'standard-information', 'standard', 'organize',
                              'standard-system', 'standard-log']
        self.monitor_list = ['third_amenu no-children']

    def hangup_feedback(self):
        """主动挂断电话或质检电话"""
        myprint.myprint('hangup: ', self.hangup)
        if self.hangup == 'feedback':
            self.browser.find_element_by_id('topbar-func-feedback').click()
        elif self.hangup == 'send':
            self.browser.find_element_by_id('topbar-func-offcall').click()
        else:
            myprint.myprint('waiting hangup ...')

    def login_intelligent_version(self, user, password):
        """去掉验证码后直接账号密码登录、"""
        self.browser.get(self.login_url)
        myprint.myprint('input username: ', user)
        self.browser.find_element_by_name('LoginForm[username]').send_keys(user)
        myprint.myprint('input password: ', password)
        self.browser.find_element_by_name('LoginForm[password]').send_keys(password)
        self.browser.find_element_by_id('login_btn').click()
        self.browser.implicitly_wait(10)

    # def login_intelligent_version(self, cookie, login_url=None):
        # 使用cookie登录、需要cookie
        # if not login_url:
        #     login_url = self.login_url
        # self.browser.get(login_url)
        # cookie_dict = {"name": "PHPSESSID", "value": cookie}
        # self.browser.add_cookie(cookie_dict)
        # self.browser.refresh()
        # # time.sleep(3)

    def top_search_input(self, number):
        """在快速拨号中输入信息"""
        self.browser.find_element_by_id("top_search").clear()
        myprint.myprint('input number ', number)
        self.browser.implicitly_wait(10)
        self.browser.find_element_by_id("top_search").send_keys(number)

    def out_call(self, *args):
        """普通呼出"""
        callee, sleep = args[0]
        myprint.myprint('out call', callee)
        self.top_search_input(str(callee))
        self.browser.find_elements_by_id("topbar-func-call")[1].click()
        myprint.myprint('begin sleep: ', sleep)
        time.sleep(sleep)
        self.hangup_feedback()

    def out_three_party(self, *args):
        """呼出/分机的三方通话"""
        callee, sleep1, threenum, sleep2 = args[0]
        tmp_hangup = self.hangup
        self.hangup = None
        self.out_call([callee, sleep1])
        myprint.myprint('begin out_three_party')
        self.top_search_input(str(threenum))
        # linux上直接点击居然会报错、手动执行js把三方通话的按钮弄出来吧、、
        js = "document.getElementsByClassName('thatCall')[0].parentElement.style='display:block'"
        self.browser.execute_script(js)
        self.browser.find_element_by_class_name("thatCall").click()
        myprint.myprint('begin sleep', sleep2)
        time.sleep(sleep2)
        self.hangup = tmp_hangup
        self.hangup_feedback()

    def in_three_party(self, *args):
        """呼入的三方通话、web振铃时没有接听、接听由sipp接听、"""
        callee, sleep = args[0]
        myprint.myprint('begin in_three_party')
        self.top_search_input(str(callee))
        # linux上直接点击居然会报错、手动执行js把三方通话的按钮弄出来吧、、
        js = "document.getElementsByClassName('thatCall')[0].parentElement.style='display:block'"
        self.browser.execute_script(js)
        self.browser.find_element_by_class_name("thatCall").click()
        myprint.myprint('begin sleep', sleep)
        time.sleep(sleep)
        self.hangup_feedback()

    def queue_pick_up(self,  *args):
        """抢接队列中的电话、"""
        queue, caller, sleep = args[0]
        # 进入监控中心
        self.browser.find_elements_by_class_name('menu-title')[self.menu_sub_list.index('monitor')].click()
        myprint.myprint('cd monitor')
        # 进入队列监控
        self.browser.find_element_by_link_text('队列监控').click()
        myprint.myprint('cd queue_monitor')
        self.browser.switch_to.frame('iframe_monitor_queue')
        myprint.myprint('switch monitor_queue')
        # 点击队列监控中的队列
        myprint.myprint('sleep 3')
        time.sleep(3)
        #self.browser.implicitly_wait(10)
        self.browser.find_element_by_id(str(queue)).click()
        myprint.myprint('click queue ', queue)
        #self.browser.implicitly_wait(10)
        # 抢接电话、
        self.browser.find_element_by_link_text(str(caller)).click()
        myprint.myprint('begin pick up ', caller)
        self.browser.switch_to.parent_frame()
        myprint.myprint('sleep time', sleep)
        time.sleep(sleep)
        self.hangup_feedback()

    def quit(self, t=0):
        """退出浏览器"""
        time.sleep(t)
        self.browser.quit()

    def cdr_info(self):
        self.browser.find_elements_by_class_name('menu-title')[self.menu_sub_list.index('report-calldetails')].click()
        self.browser.find_element_by_css_selector('a[data-id="report-calldetails"][target="main"]').click()
        self.browser.find_element_by_link_text('通话记录').click()
        self.browser.switch_to.frame('iframe_report_cdr_merge')
        self.browser.find_element_by_css_selector('a[data-id="report_cdr_index"]').click()
        self.browser.switch_to.parent_frame()
        self.browser.find_element_by_id("onoff").click()
        self.browser.find_element_by_css_selector('i[class="panel_switch"][id="panel_switch"]').click()


if __name__ == '__main__':
    login_admin = CallScenario("192.168.18.37")
    login_admin.login_intelligent_version('admin', 'admin')
    login_admin.queue_pick_up((911, 13058505211, 20))
    #login_admin.cdr_info()
    login_admin.quit(3)

