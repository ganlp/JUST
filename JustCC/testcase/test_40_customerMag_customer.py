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

    def test_customer_modify(self):  #修改客户资料-设置为私有##
        '''修改客户资料-设置为私有'''
        self.login_with_cookie()
        customer_page = customerPage.CustomerPage(self.dr)
        is_private = customer_page.modify_customer()
        self.assertEqual(is_private, "私有")

    def test_customer_del(self):  #删除客户资料##
        '''删除客户资料'''
        self.login_with_cookie()
        customer_page = customerPage.CustomerPage(self.dr)
        l = customer_page.del_customer()
        self.assertEqual(l[0]-1, l[1])
        
    def test_customer_del_from_recycle(self):  #从回收站删除客户资料##
        '''从回收站删除客户资料'''
        self.login_with_cookie()
        customer_page = customerPage.CustomerPage(self.dr)
        l = customer_page.del_customer_from_recycle()
        self.assertEqual(l[0]-1, l[1])
        
if __name__=='__main__':
    unittest.main()