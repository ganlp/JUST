import unittest

import sys
sys.path.append('../')
from public.pages import queuePage
from public.common import mytest_admin


class TestQueue(mytest_admin.MyTest):
    """队列测试"""
    def test_add_queue(self):#添加队列901-同时振铃##
        """添加队列901-同时振铃"""
        self.login_admin_with_cookie()
        queue_page = queuePage.queuePage(self.dr)
        cnt=queue_page.add_queue()
        self.assertEqual(cnt,1)

if __name__=='__main__':
    unittest.main()