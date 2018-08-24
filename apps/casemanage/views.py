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


@csrf_exempt
def test_api(request):
    if 'data' in request.POST:
        data = request.POST['data']
        process_data=data.split(',')
        for i in process_data:
            if i=='menu':
                process_data.remove(i)
      #  print(process_data,type(process_data))
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
  #      print(globalparam.case_path+"\\"+"casedata2.json")
        with open(globalparam.json_path+"\\"+"casedata2.json", 'w',encoding='utf-8') as json_file:
            json_file.write(json_str)
     #   print(json_str)
        #执行自动化测试用例
        print("================================start=================================")
        loader=subprocess.Popen(["C:\Python36\python.exe",globalparam.run_path])
        returncode=loader.wait()
        print("returncode=%s" %(returncode))

    else:
        print("not found data param")
    return JsonResponse({"result": 0, "msg": "执行成功"})

@csrf_exempt
def read_log(request):
    dirs = os.listdir(globalparam.log_path)
    dirs.sort()
    logname = dirs[-1]
    print(globalparam.log_path+"\\"+logname)
    with open(globalparam.log_path+"\\"+logname,'r',encoding='utf-8') as f:
         lines=f.readlines()[-5:]
    print(lines)
    context={"data":lines}
    return JsonResponse(context)

class testView(BaseAdminView):
    def get(self,request,*args,**kwargs):
        return render(request, 'case_view.html') #,{'data':data}
       # return HttpResponse("Hello Django!")

if __name__=='__main__':
    read_log()