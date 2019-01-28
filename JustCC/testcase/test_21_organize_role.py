import unittest

import sys
sys.path.append('../')
from public.pages import rolePage
from public.common import mytest
from time import sleep

class TestRole(mytest.MyTest):
    """角色测试"""
    def test_role_add(self):#添加角色##
        """添加角色"""
        self.login_with_cookie()
        role_page=rolePage.RolePage(self.dr)
        l=role_page.add_role()
        self.assertEqual(l[0]+1,l[1])
        
    def test_role_modify(self):#修改角色-开启号码隐藏且修改数据范围##
        """修改角色-开启号码隐藏且修改数据范围"""
        self.login_with_cookie()
        role_page=rolePage.RolePage(self.dr)
        status=role_page.modify_role()
        self.assertEqual(status,'是')
        
    def test_role_del(self):#删除角色##
        """删除角色"""
        self.login_with_cookie()
        role_page = rolePage.RolePage(self.dr)
        l = role_page.del_role()
        self.assertEqual(l[0]-1,l[1])