import sys
sys.path.append('../')
from public.pages import loginPage
from public.common import datainfo
from public.common import mytest
import unittest
from time import sleep
from config import globalparam

class Login(mytest.MyTest):
    """登录测试"""
    def test_static_login(self):#静态登录-用户名密码正确##
        """静态登录-用户名密码正确"""
        self.login_page=loginPage.LoginPage(self.dr)
        datas = datainfo.get_xls_to_dict('data_info.xlsx','login_data')
        print(datas)
        self.login_page.static_login(str(datas[1]['username']).split('.')[0],str(datas[1]['password']).split('.')[0])
        sleep(2)
        # self.cookies=self.dr.origin_driver.get_cookies()
        # with open(globalparam.cookie_path,'w') as f:
        #      f.write(str(self.cookies))

        self.assertIn('集时通讯智能版',self.login_page.return_title())

if __name__=='__main__':
    unittest.main()