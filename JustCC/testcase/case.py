import os,re,json
import sys

######################解决cmd下执行该脚本提示import error的问题
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
###############################################################

from config import globalparam

menu={
    'organize':'组织机构',
    'login':'登录',
    'staticlogin':'静态登录',
    'user':'用户管理',
    'depart':'部门管理',
    'call':'话务管理',
    'toolbar':'话务条',
    'admin':'后台管理',
    'exten':'分机管理',
	'queue':"队列管理",
    'trunk':"中继线路",
    'customerMag':'客户管理',
    'customer':'客户资料',
    'callinrule':'呼入规则',
    'calloutrule':'呼出规则',
    'ticket':'工单管理',
    'role':"角色管理",
	'dimission':"离职库",
    'manualoutcall':"人工外呼",
    "classify":"电销分类",
    "task":"项目管理"
}

class Case():
    def get_case_name(self):
        file_list=os.listdir(globalparam.case_path)
        file_list.sort()
        case_menu={}
        name_dict={}
        case_tree=[]
        for file in file_list:
            if(file[:4]=="test"):
                case_dict={}
                firstclass=file.split('_')[2]
                firstclass_name=menu[firstclass]
                secondclass=file[:-3].split('_')[3]
                secondclass_name=menu[secondclass]

                with open(globalparam.case_path+"\\"+file,'r', encoding='UTF-8') as f:
                    str=f.read()
                    menu_dict={}
                    menu_list=[]
                    classname=re.findall(r'(class.*?\()',str)[0][6:].split('(')[0]   #匹配类名
                    namelist=re.findall(r'(test_.*?##)',str)    #匹配用例名
                    for i in namelist:
                        menu_dict={}
                        menu_dict["id"]=i.split('#')[0][:-7]
                        menu_dict["name"]=i.split('#')[1]
                        menu_list.append(menu_dict)
                    name_list=[key for key in menu_dict]
                    name_list.insert(0,classname)
                    name_dict[file.split('.')[0]]=name_list
                    print(name_list)
                    case_tmp_dict={"file":file[:-3]+'('+classname+')' ,"name":secondclass_name,"case":menu_list}
                    if firstclass_name not in case_menu.keys():
                        case_menu[firstclass_name]=[case_tmp_dict]
                        case_dict["firstclass"]= firstclass_name
                        case_dict["secondclass"]=case_menu[firstclass_name]
                        case_tree.append(case_dict)
                    else:
                        case_menu[firstclass_name].append(case_tmp_dict)

        json_str = json.dumps(case_tree,ensure_ascii=False,indent=4)
        with open(globalparam.json_path+"\\"+'case_name.json', 'w',encoding='utf-8') as json_file:
            json_file.write(json_str)
        return name_dict

if __name__=='__main__':
    case=Case()
    case.get_case_name()




