###################################################################
# File Name: get_all.py
# Author: jiangtao
# mail: vlan945@163.com
# Created Time: 2018年08月20日 星期一 16时05分18秒
#=============================================================
#!/usr/bin/env python

import yaml

with open('re_custom.yaml') as f:
	x = yaml.load(f)

for i in x:
	print(i)
print("\033[31mtotol: %s\033[0m" % len(x))
