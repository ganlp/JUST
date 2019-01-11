import unittest

import sys
sys.path.append('../')
<<<<<<< HEAD
from public.pages import ticketPage
from public.common import datainfo
from public.common import mytest

class TestTicket(mytest.MyTest):
    '''工单管理测试'''
    def test_1_add_ticket_type(self):#添加工单类型##
        '''添加工单类型'''
        self.login_with_cookie()
        ticket_page = ticketPage.TicketPage(self.dr)
        cnt= ticket_page.add_ticket_type()
        self.assertEqual(cnt, 1)

    def test_2_add_ticket(self):#创建工单##
        '''创建工单'''
        self.login_with_cookie()
        ticket_page = ticketPage.TicketPage(self.dr)
        cnt= ticket_page.add_ticket()
        print(cnt)
        self.assertEqual(cnt, 1)
    
=======
from public.pages import customerPage
from public.common import datainfo
from public.common import mytest

class TestCustomer(mytest.MyTest):
    '''客户资料测试'''
    def test_customer_add(self):#添加客户资料##
        '''添加客户资料'''
        self.login_with_cookie()
        customer_page = customerPage.CustomerPage(self.dr)
        cnt= customer_page.add_customer()
        self.assertEqual(cnt, 1)

>>>>>>> github/master
if __name__=='__main__':
    unittest.main()