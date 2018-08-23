import unittest

import sys
sys.path.append('../')
from public.pages import userPage
from public.common import datainfo
from public.common import mytest
from time import sleep

class TestUser(mytest.MyTest):
    """用户测试"""
    def atest_user_add(self):#添加用户##
        """添加用户"""
        self.login_with_cookie()
        user_page=userPage.UserPage(self.dr)
        datas = datainfo.get_xls_to_dict('data_info.xlsx','user_data')
        for data in datas:
            l=user_page.add_user(str(data['work_no']).split('.')[0],data['work_name'],data['username'])
            self.assertEqual(l[0]+1,l[1])
            self.dr.wait(5)
            sleep(3)

    def test_user_del(self):#删除用户##
        """删除用户"""
        self.login_with_cookie()
        user_page=userPage.UserPage(self.dr)
        l=user_page.del_user(3)
        self.assertEqual(l[0]-1,l[1])

if __name__=='__main__':
    unittest.main()