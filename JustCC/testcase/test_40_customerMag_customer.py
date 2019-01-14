import unittest

import sys
sys.path.append('../')
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
        
    def test_depart_add(self):  # 添加部门##
        '''添加客户资料'''
        self.login_with_cookie()
        customer_page = customerPage.CustomerPage(self.dr)
        l = customer_page.add_customer()
        self.assertEqual(l[0] + 1, l[1])


if __name__=='__main__':
    unittest.main()