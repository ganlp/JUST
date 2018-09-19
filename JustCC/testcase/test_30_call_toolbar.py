import unittest

import sys
sys.path.append('../')
from public.pages import toolbarPage
from public.common import datainfo
from public.common import mytest

class TestToolbar(mytest.MyTest):
    """话务条测试"""
    def test_quick_call(self):#快速拨号##
        """快速拨号"""
        self.login_with_cookie()
        toolbar_page=toolbarPage.ToolbarPage(self.dr)
        toolbar_page.quick_call()
    #    self.drpages.F5()
    #    self.assertIsNotNone(self.dr.get_element("css->.stext ringing"),'未振铃')


if __name__=='__main__':
    unittest.main()