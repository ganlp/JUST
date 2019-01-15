import unittest

import sys
sys.path.append('../')
from public.pages import callOutPage
from public.common import mytest_admin
from public.common import datainfo

class TestCallout(mytest_admin.MyTest):
    """呼出规则"""
    def test_calloutrule(self):#添加呼出规则##
        """添加呼出规则"""
        self.login_admin_with_cookie()
        call_outpage = callOutPage.CallOutPage(self.dr)
        cnt = call_outpage.add_calloutrule()

