import unittest

import sys
sys.path.append('../')

from public.pages import ticketPage
from public.common import datainfo
from public.common import mytest

class TestTicket(mytest.MyTest):
    '''工单管理测试'''
    def test_add_ticket_type(self):#添加工单类型##
        '''添加工单类型'''
        self.login_with_cookie()
        ticket_page = ticketPage.TicketPage(self.dr)
        cnt= ticket_page.add_ticket_type()
        self.assertEqual(cnt, 1)
        
    def test_add_ticket_workflow_conf(self):#创建工作流##
        '''创建工作流'''
        self.login_with_cookie()
        ticket_page = ticketPage.TicketPage(self.dr)
        cnt = ticket_page.add_ticket_workflow_conf()
        self.assertEqual(cnt, 2)

    def test_add_ticket_new(self):#创建工单-新建状态##
        '''创建工单-新建状态'''
        self.login_with_cookie()
        ticket_page = ticketPage.TicketPage(self.dr)
        cnt= ticket_page.add_ticket_new()
        self.assertEqual(cnt, 1)
        
    def test_add_ticket_process(self):#创建工单-处理中状态##
        '''创建工单-处理中状态'''
        self.login_with_cookie()
        ticket_page = ticketPage.TicketPage(self.dr)
        cnt = ticket_page.add_ticket_process()
        self.assertEqual(cnt, 1)
        
    def test_add_ticket_solve(self):#创建工单-已解决状态##
        '''创建工单-已解决状态'''
        self.login_with_cookie()
        ticket_page = ticketPage.TicketPage(self.dr)
        cnt = ticket_page.add_ticket_solve()
        self.assertEqual(cnt, 1)
        
    def test_add_ticket_finish(self):#创建工单-完结状态##
        '''创建工单-完结状态'''
        self.login_with_cookie()
        ticket_page = ticketPage.TicketPage(self.dr)
        cnt= ticket_page.add_ticket_finish()
        self.assertEqual(cnt, 1)

    def test_add_ticket_attachment(self):#创建新建状态工单-带附件##
        '''创建新建状态工单-带附件'''
        self.login_with_cookie()
        ticket_page = ticketPage.TicketPage(self.dr)
        cnt = ticket_page.add_ticket_attachment()
        self.assertEqual(cnt, 1)
        
    def test_handle_ticket(self):#处理工单-处理成完结状态##
        '''处理工单-处理成完结状态'''
        self.login_with_cookie()
        ticket_page = ticketPage.TicketPage(self.dr)
        status=ticket_page.handle_ticket()
        self.assertEqual(status,"完结")
        
    def test_add_ticket_with_workflow(self):#创建新建状态工单-带工作流##
        '''创建新建状态工单-带工作流'''
        self.login_with_cookie()
        ticket_page = ticketPage.TicketPage(self.dr)
        cnt = ticket_page.add_ticket_with_workflow()
        self.assertEqual(cnt, 1)
        
    def test_del_ticket(self):#删除工单##
        '''删除工单'''
        self.login_with_cookie()
        ticket_page = ticketPage.TicketPage(self.dr)
        l = ticket_page.del_ticket()
        self.assertEqual(l[0]-1,l[1])
        
