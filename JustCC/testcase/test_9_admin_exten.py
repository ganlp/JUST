import unittest

import sys
sys.path.append('../')
from public.pages import extenPage
from public.common import mytest_admin


class TestExten(mytest_admin.MyTest):
    """分机测试"""
    def test_add_exten(self):#添加分机##
        """添加分机"""
        self.login_admin_with_cookie()
        exten_page = extenPage.ExtenPage(self.dr)
        cnt=exten_page.add_exten()
        self.assertEqual(cnt,1)

if __name__=='__main__':
    unittest.main()