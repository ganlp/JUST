import unittest

import sys
sys.path.append('../')
from public.pages import departmentPage
from public.common import mytest


class TestDepart(mytest.MyTest):
    '''部门测试'''
    def test_depart_add(self):#添加部门##
        '''添加部门'''
        self.login_with_cookie()
        depart_page=departmentPage.DepartPage(self.dr)
        l=depart_page.add_depart()
        self.assertEqual(l[0]+1,l[1])

    def test_depart_del(self):#删除部门##
        """删除部门"""
        self.login_with_cookie()
        depart_page=departmentPage.DepartPage(self.dr)
        l=depart_page.del_depart()
        self.assertEqual(l[0]-1,l[1])

if __name__=='__main__':
    unittest.main()
