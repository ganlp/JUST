import unittest

import sys
sys.path.append('../')
from public.pages import dimissionPage
from public.common import datainfo
from public.common import mytest
from time import sleep

class TestDimission(mytest.MyTest):
    """离职库测试"""
    def test_del_dimission(self):#从离职库中删除用户##
        """从离职库中删除用户"""
        self.login_with_cookie()
        user_page=dimissionPage.DimissionPage(self.dr)
        l=user_page.delete_dimission()
        self.assertEqual(l[0]-1,l[1])
        
    def test_revover_dimission(self):#从离职库中还原用户##
        """从离职库中还原用户"""
        self.login_with_cookie()
        user_page=dimissionPage.DimissionPage(self.dr)
        l=user_page.recover_dimission()
        self.assertEqual(l[0]-1,l[1])