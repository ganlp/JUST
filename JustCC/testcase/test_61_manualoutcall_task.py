import unittest

import sys
sys.path.append('../')

from public.pages import outcallTaskPage
from public.common import mytest

class ManualoutcallClassify(mytest.MyTest):
    '''人工外呼-项目管理'''
    def test_add_task(self):#添加项目##
        '''添加项目'''
        self.login_with_cookie()
        outcalltask_page = outcallTaskPage.OutcallTaskPage(self.dr)
        l= outcalltask_page.add_task()
        self.assertEqual(l[0]+1, l[1])