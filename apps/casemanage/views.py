from django.shortcuts import render
from xadmin.views import BaseAdminView
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from dss.Serializer import serializer
from rest_framework.views import APIView
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json,sys,os,subprocess
from JustCC.config import globalparam
from django.http import JsonResponse
import time

@csrf_exempt
def set_serverip(request):      #传递设置的被测服务器IP值
    print(request.POST)
    if 'data' in request.POST:
        serverip = request.POST['data']
        print(serverip)
        defaultip = globalparam.server_addr[7:]
        file_data = ""
        with open(globalparam.config_file_path + "\\" + "globalparam.py", 'r', encoding='UTF-8') as f:
            for line in f:
                if defaultip in line:
                    line = line.replace(defaultip, serverip)
                file_data += line
        with open(globalparam.config_file_path + "\\" + "globalparam.py", 'w', encoding="utf-8") as f:
            f.write(file_data)
        return JsonResponse({"result": 0, "msg": "执行成功"})
    else:
        print("not found data param")
        return JsonResponse({"result": 1, "msg": "执行失败"})

@csrf_exempt
def test_api(request):    #调接口传选中的用例数据
    if 'data' in request.POST:
        data = request.POST['data']
        process_data=data.split(',')
        for i in process_data:
            if i=='menu':
                process_data.remove(i)
        json_list=[]
        for i in range(len(process_data)):
            if '(' in process_data[i]:
                json_dict={"case":[]}
                json_dict["filename"]=process_data[i].split('(')[0]
                json_dict["class"]=process_data[i].split('(')[1].strip(')')
                cnt=1
                while i+cnt<len(process_data) and '(' not in process_data[i+cnt]:
                    json_dict["case"].append({"id":process_data[i+cnt]})
                    cnt+=1
                i+=cnt
                json_list.append(json_dict)
        json_str = json.dumps(json_list,ensure_ascii=False,indent=4)
        with open(globalparam.json_path+"\\"+"casedata2.json", 'w',encoding='utf-8') as json_file:
            json_file.write(json_str)
     #   print(json_str)
        #执行自动化测试用例
        print("================================start=================================")
        loader=subprocess.Popen(["C:\Python36\python.exe",globalparam.run_path])
        returncode=loader.wait()
        print("returncode=%s" %(returncode))
        return JsonResponse({"result": 0, "msg": "执行成功"})
    else:
        print("not found data param")
        return JsonResponse({"result": 1, "msg": "执行失败"})


def  current_log_lines():     #记录当前日志行数
    now_day=time.strftime("%Y-%m-%d")
    dirs = os.listdir(globalparam.log_path)
    dirs.sort()
    logname = dirs[-1]
    # print(globalparam.log_path+"\\"+logname)
    if logname.split('.')[0]==now_day:
        with open(globalparam.log_path + "\\" + logname, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return len(lines)
    else:
        return 0

def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

@csrf_exempt
@static_vars(counter=current_log_lines())  #设置counter为静态变量,每调用此方法一次在上次基础上累加
def read_log(request):
    if(read_log.counter==0):
        return JsonResponse({"data":'.'})
    else:
        dirs = os.listdir(globalparam.log_path)
        dirs.sort()
        logname = dirs[-1]
        #print(globalparam.log_path+"\\"+logname)
        with open(globalparam.log_path + "\\" + logname, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        if len(lines)> read_log.counter:
            context={"data":'\n'+lines[read_log.counter]}
            read_log.counter+=1
            return JsonResponse(context)
        else:
            return JsonResponse({"data":'.'})

class testView(BaseAdminView):
    def get(self,request,*args,**kwargs):
        return render(request, 'case_view.html') #,{'data':data}
       # return HttpResponse("Hello Django!")

if __name__=='__main__':
     pass