# -*- coding:utf-8 -*-
# author:jiangtao

import yaml
import json
import subprocess
import pass_auth_code
import time


class Myerror(Exception):
    """自定义一个异常"""
    def __init__(self, msg):
        self.msg = msg
        Exception.__init__(self, self.msg)


def parse_dict(dictionary, key_word):
    """
    判断一个dictionary中key对应的value是否为空、为空报错、不为空返回value
    :param dictionary: 要检查的字典
    :param key_word: 要检查的key
    :return: key 对应的value、
    """
    if dictionary.get(key_word):
        return dictionary.get(key_word)
    raise Myerror(key_word + " can't be null")


class ParseYaml(object):
    def __init__(self, file):
        self.file = file

    def get_dict(self):
        with open(self.file, encoding='utf-8') as f:
            return yaml.load(f)

    def josn_dict(self):
        with open(self.file, encoding='utf-8') as f:
            return json.load(f)


class CreateScenario(object):
    """根据基础的7个标准xml生成万万千的scenario"""
    def __init__(self, filename, path='../etc/standard_xml/'):
        self.filename = filename
        self.path = path
        self.info_str = ''

    @staticmethod
    def parse_time_wait(wait_time):
        """
        用于生成scenario的通话时间、
        :param wait_time: 传入一个数字
        :return: 返回字符串
        """
        return '\n\t<pause milliseconds="{}"/>\n'.format(wait_time)

    @staticmethod
    def parse_button(button_num, button_interval=350):
        """
        用于生成scenario的按键信息、
        :param button_num: button的值、
        :param button_interval: 按键间隔时间
        :return:
        """
        button_key_str = ''
        for i in str(button_num):
            if i == 's':
                button_key = "start"
            elif i == 'p':
                button_key = "pound"
            elif i.isalnum():
                button_key = i
            else:
                raise TypeError
            button_key_str += """

    <!-- ############################ begin button {key} ############################ -->
    <nop>
        <action>
            <exec play_pcap_audio="../lib/pcap/dtmf_2833_{key}.pcap"/>
        </action>
    </nop>

    <pause milliseconds="{button_interval}"/>

    <nop>
        <action>
            <exec play_pcap_audio="../lib/pcap/g711a.pcap"/>
        </action>
    </nop>
    <!-- ############################ end button {key} ############################ -->

    """.format(key=button_key, button_interval=button_interval)
        return button_key_str

    def parse_call_options(self, call_options, button_interval=350):
        """
        分析yaml中的call_options、如果是time、则写暂停时间、如果是button则写按键、
        :param call_options: 呼叫选项的值、传入的是一个列表、一个列表中的值一个dict、[{ time: 30000}, { code: 486 } ]
        :param button_interval: 按键间隔
        :return:
        """
        if call_options:
            for option in call_options:
                time_value = option.get('time')
                button_value = option.get('button')
                if time_value:
                    self.info_str += self.parse_time_wait(time_value)
                elif button_value:
                    self.info_str += self.parse_button(button_value, button_interval)
                else:
                    raise Myerror('未知选项call_options ..')
            return self.info_str

    def pasere_str(self, dst_path, keyword='<!--custom-->'):
        """
        将数据写入新的xml、
        :param dst_path: 生成文件存放的路径、
        :param info_str: 要替换的关键字、
        :param keyword: 过滤的关键字、
        :param replace: 是否将字符串与关键字直接替换、
        :return:
        """
        with open(self.path + self.filename, encoding='utf-8') as src:
            all_info = src.read()
            insert_index = all_info.find(keyword)
            if insert_index == -1:
                raise Myerror("can't find %s in %s, insert failed .. " % (keyword, self.path + self.filename))
            all_info = all_info[:insert_index+len(keyword)] + self.info_str + all_info[insert_index+len(keyword):]
            with open(dst_path, 'w', encoding='utf-8') as dst:
                dst.write(all_info)
                

def create_scenario(srcfile, dstfile, options, src_path='../etc/standard_xml/', button_interval=350):
    """
    生成scenario文件、
    :param srcfile: 源文件名
    :param dstfile: 生成的目标地址、
    :param options: 根据选项生成不同内容的scenario-数据类型：list
    :param src_path: 根据什么源文件所在路径
    :param button_interval: 按键间隔
    :return:
    """
    pares_stad_xml = CreateScenario(srcfile, src_path)
    pares_stad_xml.parse_call_options(options, button_interval)
    pares_stad_xml.pasere_str(dstfile)


class PrepareSippTest(object):
    def __init__(self, conf_dict=None):
        self.cmd_str = "sipp"
        self.csv_str = "SEQUENTIAL\n"
        self.sleep = conf_dict.get('sleep')
        if self.sleep:
            self.cmd_str = "sleep %s && %s" % (self.sleep, self.cmd_str)
        self.web_confs = conf_dict.get('web_action')
        if self.web_confs:
            self.web_sleep = conf_dict.get('web_sleep') or 0
            self.web_action = conf_dict['web_action'] or 'quit'
            self.web_info = conf_dict['web_info']
            self.web_ip = self.web_info['web_ip']
            self.web_port = self.web_info.get('web_port') or 80
            self.web_user = self.web_info.get('web_user') or 'admin'
            self.web_pwd = self.web_info.get('web_pwd') or 'admin'
            self.web_hangup = conf_dict.get('web_hangup') or 'wait'
            self.web_args = conf_dict['args']
            start = time.time()
            self.login_web = pass_auth_code.CallScenario(self.web_ip, self.web_port)
            self.login_web.hangup = self.web_hangup
            self.login_web.login_intelligent_version(self.web_user, self.web_pwd)
            print("login web time: %s" % (time.time()-start))
        else:
            self.server_info = parse_dict(conf_dict, 'server_info')
            self.local_info = parse_dict(conf_dict, 'local_info')
            self.call_type = parse_dict(conf_dict, 'call_type')
            self.hangup = parse_dict(conf_dict, 'hangup')
            self.call_info = parse_dict(conf_dict, 'call_info')
            self.call_options = conf_dict.get('call_options')
            self.sipp_options = parse_dict(conf_dict, 'sipp_options')
            self.sipp_file = parse_dict(conf_dict, 'sipp_file')
            self.xml_path = parse_dict(self.sipp_file, 'xml')
            self.csv_path = parse_dict(self.sipp_file, 'csv')
            self.canrun = ''

    def exec_web_action(self):
        func = getattr(self.login_web, self.web_action)
        print('sleep %s before exec %s' % (self.web_sleep, self.web_action))
        print(self.web_args)
        time.sleep(self.web_sleep)
        func(self.web_args)
        self.login_web.quit()

    def parse_server_info(self):
        """
        处理server_info信息、并将信息追加到self.cmd_str中、
        :return:
        """
        server_ip = parse_dict(self.server_info, 'ip')
        server_port = parse_dict(self.server_info, 'port')
        self.cmd_str += " %s:%s" % (server_ip, server_port)
        return server_ip, server_port

    def parse_local_info(self):
        """
        处理local_info信息、并将信息追加到self.cmd_str中、
        :return:
        """
        local_ip = parse_dict(self.local_info, 'ip')
        local_port = parse_dict(self.local_info, 'port')
        self.cmd_str += " -i %s -p %s" % (local_ip, local_port)
        return local_ip, local_port

    def parse_sipp_file(self):
        self.cmd_str += ' -sf %s -inf %s' % (self.xml_path, self.csv_path)

    def parse_sipp_options(self):
        """
        处理 yaml文件中的sipp_options信息、并追加到self.cmd_str中、
        :return:
        """
        for i in self.sipp_options:
            if isinstance(i, dict):
                option, value = list(i.items())[0]
                self.cmd_str += ' %s %s' % (option, value)
            elif isinstance(i, str):
                self.cmd_str += ' %s' % i

    def registry(self, callee):
        csv_file = '../user_scenario/registry/%s.csv' % callee
        with open(csv_file, 'w', encoding='utf-8') as f:
            reg_str = "SEQUENTIAL\n{0};[authentication username={0} password={0}]\n".format(callee)
            f.write(reg_str)
        cmd_str = 'sipp %s:%s -i %s -p %s -sf %s -inf %s -m 1 -aa' % (
            self.server_info['ip'], self.server_info['port'], self.local_info['ip'], self.local_info['port'],
        '../etc/standard_xml/register.xml', csv_file)
        print(cmd_str)
        status, stdout = subprocess.getstatusoutput(cmd_str)
        return status

    def no_add_option(self, caller, callee):
        if self.call_type == 'outgoing':
            self.csv_str += '{0};[authentication username={0} password={0}];{1}\n'.format(caller, callee)
        elif self.call_type in ['incoming', 'ringexten']:
            print(self.call_type)
            self.csv_str += '%s;%s\n' % (caller, callee)

    def parse_call_type(self, add_flag, caller, callee, add_num, add_step):
        """
        根据calltype和add_type得出的add_flag、处理后将信息追加到self.csv_str中去、
        :param add_flag: 1-只加被叫且只有被叫、2-主叫被叫全加、3-只加主叫、4-只加被叫
        :param caller: 主叫号码
        :param callee: 被叫号码
        :param add_num: 要迭代的次数、
        :param add_step: 要迭代的步长
        :return:
        """
        flag_zero = lambda x: int(str(x)[0]) == 0  # 匿名函数、判断是号码是否已0开头、是返回True、
        if add_flag == 1:
            if add_step and add_num:
                for i in range(0, add_num * add_step, add_step):
                    callee_temp = int(callee) + i
                    if flag_zero(callee):
                        callee_temp = '0' + str(callee_temp)
                    self.csv_str += '%s\n' % callee_temp
            else:
                self.csv_str += '%s\n' % callee
        elif add_flag == 2:
            if add_step and add_num:
                for i in range(0, add_step * add_num, add_step):
                    caller_temp, callee_temp = int(caller) + i, int(callee) + i
                    if flag_zero(caller):
                        caller_temp = '0' + str(caller_temp)
                    if flag_zero(callee):
                        callee_temp = '0' + str(callee_temp)
                    if self.call_type == 'outgoing':
                        self.csv_str += '{0};[authentication username={0} password={0}];{1}\n'.format(caller_temp, callee_temp)
                    elif self.call_type == 'incoming' or self.call_type == 'ringexten':
                        self.csv_str += '%s;%s\n' % (caller_temp, callee_temp)
            else:
                self.no_add_option(caller, callee)
        elif add_flag == 3:
            if add_step and add_num:
                for i in range(0, add_num * add_step, add_step):
                    caller_temp = int(caller) + i
                    if flag_zero(caller):
                        caller_temp = '0' + str(caller_temp)
                    if self.call_type == 'outgoing':
                        self.csv_str += '{0};[authentication username={0} password={0}];{1}\n'.format(caller_temp, callee)
                    elif self.call_type == 'incoming' or self.call_type == 'ringexten':
                        self.csv_str += '%s;%s\n' % (caller_temp, callee)
            else:
                self.no_add_option(caller, callee)
        elif add_flag == 4:
            if add_step and add_num:
                for i in range(0, add_num * add_step, add_step):
                    callee_temp = int(callee) + i
                    if flag_zero(callee):
                        callee_temp = '0' + str(callee_temp)
                    if self.call_type == 'outgoing':
                        self.csv_str += '{0};[authentication username={0} password={0}];{1}\n'.format(caller, callee_temp)
                    elif self.call_type == 'incoming' or self.call_type == 'ringexten':
                        self.csv_str += '%s;%s\n' % (caller, callee_temp)
            else:
                self.no_add_option(caller, callee)
        else:
            raise Myerror('add_flag unknown')

    def parse_call_info(self):
        for info in self.call_info:
            add_type = info.get('add_type') or ''
            add_step = info.get('add_step') or ''
            add_num = info.get('add_num') or ''
            add_flag = 2
            if self.call_type == "answer" or self.call_type == "noanswer":
                callee = parse_dict(info, 'callee')
                reg_status = self.registry(callee)
                if reg_status != 0:
                    pass
                    # raise Myerror("%s registry faild.." % callee)
                caller = None
                add_flag = 1  # 只加被叫、并且只有被叫、
                self.parse_call_type(add_flag, caller, callee, add_num, add_step)
            elif self.call_type == 'outgoing' or self.call_type == 'incoming' or self.call_type == 'ringexten':
                caller = parse_dict(info, 'caller')
                callee = parse_dict(info, 'callee')
                if add_type == 'all':
                    add_flag = 2  # 主叫被叫都加、
                elif add_type == 'caller':
                    add_flag = 3  # 只加主叫、
                elif add_type == 'callee':
                    add_flag = 4  # 只加被叫、
                self.parse_call_type(add_flag, caller, callee, add_num, add_step)

    def write_xml_csv(self):
        with open(self.csv_path, 'w', encoding='utf-8') as csv:
            csv.write(self.csv_str)

        srcfile = "%s_%s.xml" % (self.call_type, self.hangup)
        create_scenario(srcfile, self.xml_path, self.call_options)

    def prepare_run(self):
        # 生成cmd的条件
        self.parse_server_info()
        self.parse_local_info()
        self.parse_sipp_file()
        self.parse_sipp_options()
        # 生成csv的条件
        self.parse_call_info()
        # 写xml和csv
        self.write_xml_csv()
        # 返回cmd
        return self.cmd_str


if __name__ == '__main__':
    scenario_name = 'in_extenB_CFB_exten'
    parse_yaml = ParseYaml('re_custom.yaml').get_dict()[scenario_name]
    for value in parse_yaml:
        print('\033[31m[ begin prepare %s ]\033[0m'.center(50, '*') % scenario_name)
        one_scenario = PrepareSippTest(value)
        cmd_str = one_scenario.prepare_run()
        print(cmd_str)
        print('\033[31m[ end parse %s ]\033[0m'.center(50, '*') % scenario_name)
        print()

