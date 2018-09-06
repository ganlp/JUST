###################################################################
# File Name: run_sipp.py
# Author: jiangtao
# mail: vlan945@163.com
# Created Time: 2018年08月20日 星期一 14时12分18秒
# blank: 2
# =============================================================
# !/usr/bin/env python

import gevent
from gevent import monkey
monkey.patch_all()
import sys
import subprocess
import time
sys.path.append('../lib/')
import parse_custom
from myfunc import Myprint

myprint = Myprint(32)

global_timeout = 60


def exec_sipp(cmd_str):
    with gevent.Timeout(global_timeout, False) as timeout:
        status, output = subprocess.getstatusoutput(cmd_str)
        return status


def main(count, line_keys, parse_yaml):
    start = time.time()
    success_list, failed_list, all_time_list = [], [], []
    for c in range(int(count)):
        print(" 第%s次循环: [ %s ] ".center(100, '*') % (c+1, ' '.join(line_keys[0:5])))
        num = 1
        call_time_list, success_l, failed_l = [], [c+1], [c+1]
        for line_key in line_keys:
            cmd_list, web_action_list, gevent_list  = [], [], []
            try:
                print(' \033[31m[ {}-{} ]\033[0m '.format(num, line_key).center(100, ' '))
                num += 1
                startcall_time = time.time()
                value = parse_yaml[line_key]
                #if line_key == 'web_out_phone':  # 测试呼叫异常、
                #    print(1/0)
                for i in value:
                    one_scenario = parse_custom.PrepareSippTest(i)
                    if one_scenario.web_confs:
                        web_action_list = [gevent.spawn(one_scenario.exec_web_action)]
                    else:
                        cmd_str = one_scenario.prepare_run()
                        print(cmd_str)
                        cmd_list.append(cmd_str)
                gevent_list = [gevent.spawn(exec_sipp, cmd_str) for cmd_str in cmd_list]
                gevent_list = gevent_list + web_action_list
                gevent.joinall(gevent_list)
                success_l.append(line_key)
            except Exception as e:
                print(e)
                failed_l.append(line_key)
            finally:
                endcall_time = time.time()-startcall_time
                myprint.myprint('[ call use time --> %s ]' % (endcall_time))
                call_time_list.append(round(endcall_time))
        success_list.append(success_l)
        failed_list.append(failed_l)
        all_time_list.append(call_time_list)
    print(''.center(100, '#'))
    myprint.myprint("[ total time --> %s]" % (time.time()-start))
    print('\033[33mtotal [{}]:\033[0m\n\033[33msuccess [{}]:\033[0m  {}\n\033[33mfaild [{}]:\033[0m {}'.format(
        int(count)*len(line_keys), 
        sum([len(i[1:]) for i in success_list if len(i) != 1]), success_list, 
        sum([len(i[1:] or []) for i in failed_list]), failed_list))
    print('\033[33mall_time_list:\033[0m', all_time_list)
    return success_list,failed_list,all_time_list


if __name__ == '__main__':
    count = sys.argv[1] if len(sys.argv) > 1 else 3
    line_keys = sys.argv[2:] if len(sys.argv) > 1 else ['in_ivr_nobutton']
    if not count.isdigit():
        count = 1
        line_keys = sys.argv[1:]
        print("Usage: python %s {num} {[scenario [scennario]..]}" % sys.argv[0])
        # sys.exit()
    open_time = time.time()
    parse_yaml = parse_custom.ParseYaml('re_custom.yaml').get_dict()
    myprint.myprint('open file use %s' % (time.time()-open_time))
    main(count, line_keys, parse_yaml)
