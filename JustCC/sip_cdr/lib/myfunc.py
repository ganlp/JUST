###################################################################
# File Name: myfun.py
# Author: jiangtao
# mail: vlan945@163.com
# Created Time: 2018年08月28日 星期二 16时29分02秒
#=============================================================
#!/usr/bin/env python

import redis
import parse_custom


class Myprint(object):
    def __init__(self, default=37):
        self.default = default

    def myprint(self, *args):
        print("\033[%sm%s\033[0m" % (self.default, ' '.join([str(i) for i in args])))


class MyRedis(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.pool = redis.ConnectionPool(self.ip, self.port)
        self.connect = redis.Redis(self.pool)

    def set_dict(self, name, dict_obj):
        self.connect.hmset(name, dict_obj)









if __name__ == '__main__':
    for i in range(31,38):
        Myprint(i).myprint(str(i),'jiangtao', 'love', 'python')
    for i in range(41,48):
        Myprint(i).myprint(str(i),'jiangtao', 'love', 'python')


