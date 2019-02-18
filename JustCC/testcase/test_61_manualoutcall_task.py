import unittest

import sys
sys.path.append('../')

from public.pages import outcallTaskPage
from public.common import mytest

class ManualoutcallTask(mytest.MyTest):
    '''人工外呼-项目管理'''
    def test_add_task(self):#添加项目##
        '''添加项目'''
        self.login_with_cookie()
        outcalltask_page = outcallTaskPage.OutcallTaskPage(self.dr)
        l= outcalltask_page.add_task()
        self.assertEqual(l[0]+1, l[1])
        
    def test_import_number(self):#导入号码##
        '''导入号码'''
        self.login_with_cookie()
        outcalltask_page = outcallTaskPage.OutcallTaskPage(self.dr)
        outcalltask_page.import_number()
        
    def test_task_unable(self):#禁用项目##
        '''禁用项目'''
        self.login_with_cookie()
        outcalltask_page = outcallTaskPage.OutcallTaskPage(self.dr)
        status=outcalltask_page.task_unable()
        self.assertEqual(status,"启用")
        
    def test_task_enable(self):#启用项目##
        '''启用项目'''
        self.login_with_cookie()
        outcalltask_page = outcallTaskPage.OutcallTaskPage(self.dr)
        status=outcalltask_page.task_unable()
        self.assertEqual(status,"禁用")
        
    def test_task_del(self):#删除项目##
        '''删除项目'''
        self.login_with_cookie()
        outcalltask_page = outcallTaskPage.OutcallTaskPage(self.dr)
        l = outcalltask_page.task_del()
        self.assertEqual(l[0]-1, l[1])