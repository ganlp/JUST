import unittest

import sys
sys.path.append('../')
from public.pages import trunkPage
from public.common import mytest_admin
from public.common import datainfo


class TestTrunk(mytest_admin.MyTest):
    """中继测试"""
    def test_add_trunk(self):#添加中继-外部注册##
        """添加中继-外部注册"""
        self.login_admin_with_cookie()
        trunk_page = trunkPage.TrunkPage(self.dr)
        datas = datainfo.get_xls_to_dict('data_info.xlsx', 'trunk_data')[0]
        cnt = trunk_page.add_trunk(str(datas['trunkname']).split('.')[0], datas['zone'], str(datas['max_chans']).split('.')[0],datas["sip_ip"])
        self.assertEqual(cnt, 1)


if __name__=='__main__':
    unittest.main()