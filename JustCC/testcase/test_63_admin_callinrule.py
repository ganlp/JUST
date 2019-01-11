import unittest

import sys
sys.path.append('../')
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
        self.assertEqual(cnt, 1)

if __name__=='__main__':
    unittest.main()