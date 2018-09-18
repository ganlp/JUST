import unittest

import sys
sys.path.append('../')
from public.pages import extenPage
from public.common import mytest_admin


class TestExten(mytest_admin.MyTest):
    """分机测试"""
    def atest_add_exten(self):#添加分机##
        """添加分机"""
        self.login_admin_with_cookie()
        exten_page = extenPage.ExtenPage(self.dr)
        cnt=exten_page.add_exten()
        self.assertEqual(cnt,1)

    def test_del_exten(self):#删除分机##
        """删除分机"""
        self.login_admin_with_cookie()
        exten_page = extenPage.ExtenPage(self.dr)
        l=exten_page.del_exten()
        self.assertEqual(l[0]-1,l[1])

    def atest_modify_exten(self):#修改分机##
        """修改分机"""
        pass

if __name__=='__main__':
    unittest.main()