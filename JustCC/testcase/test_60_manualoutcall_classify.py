import unittest

import sys
sys.path.append('../')

from public.pages import outcallClassifyPage
from public.common import mytest

class ManualoutcallClassify(mytest.MyTest):
    '''人工外呼-电销分类'''
    def test_add_classify(self):#添加电销分类##
        '''添加电销分类'''
        self.login_with_cookie()
        manualoutcall_page = outcallClassifyPage.OutcallclassifyPage(self.dr)
        l= manualoutcall_page.add_classify()
        self.assertEqual(l[0]+1, l[1])
        
    def test_classify_disable(self):#禁用电销分类##
        '''禁用电销分类'''
        self.login_with_cookie()
        manualoutcall_page = outcallClassifyPage.OutcallclassifyPage(self.dr)
        status= manualoutcall_page.classify_disable()
        self.assertEqual(status, '禁用')