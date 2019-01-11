import unittest

import sys
sys.path.append('../')
<<<<<<< HEAD
from public.pages import callInPage
from public.common import mytest_admin
from public.common import datainfo

class TestCallin(mytest_admin.MyTest):
    """呼入规则"""
    def test_callinrule(self):#添加呼入规则##
        """添加呼入规则"""
        self.login_admin_with_cookie()
        callin_page = callInPage.CallInPage(self.dr)
        cnt = callin_page.add_callinrule()
=======
from public.pages import queuePage
from public.common import mytest_admin
from public.common import datainfo

class TestQueue(mytest_admin.MyTest):
    """队列测试"""
    def test_add_queue(self):#添加队列901-同时振铃##
        """添加队列901-同时振铃"""
        self.login_admin_with_cookie()
        queue_page = queuePage.queuePage(self.dr)
        datas = datainfo.get_xls_to_dict('data_info.xlsx', 'queue_data')[0]
        cnt = queue_page.add_queue(str(datas['queueno']).split('.')[0])
>>>>>>> github/master
        self.assertEqual(cnt, 1)

if __name__=='__main__':
    unittest.main()