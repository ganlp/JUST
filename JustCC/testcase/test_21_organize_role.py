import unittest

import sys
sys.path.append('../')
from public.pages import rolePage
from public.common import datainfo
from public.common import mytest
from time import sleep

class TestRole(mytest.MyTest):
    """角色测试"""
    def test_user_add(self):#添加角色##
        """添加角色"""
        self.login_with_cookie()
        role_page=rolePage.RolePage(self.dr)
        l=role_page.add_role()
        self.assertEqual(l[0]+1,l[1])

if __name__=='__main__':
    unittest.main()