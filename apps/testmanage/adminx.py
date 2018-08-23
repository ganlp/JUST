#coding=utf-8
#from django.contrib import admin
import xadmin
from .models import test_project,test_version,test_task
import time

# Register your models here.
class ProjectAdmin(object):
    list_display = ['name','start_time','create_person']
    search_fields = ['name']
    list_filter = ['name']
    model_icon='fa fa-thumb-tack'
    date=time.strftime("%Y-%m-%d",time.localtime(1531453664.8349574))

    # data_charts = {
    #     "project_time": {'title': u"项目", "x-field": "name", "y-field": ("date"),
    #                    "order": ('date',)
    #                    }
    # }

class VersionAdmin(object):
    list_display = ['project','name','status','start_time','create_person','desc']
    search_fields = ['project','name']
    list_filter = ['name']
    model_icon='fa fa-sign-out'

class TaskAdmin(object):
    list_display = ['version','name','start_time','res_person','status']
    search_fields = ['name']
    list_filter = ['name']
    model_icon='fa fa-star-half'
#    style_fields  = {'res_person': 'checkbox-inline', }


xadmin.site.register(test_project,ProjectAdmin)
xadmin.site.register(test_version,VersionAdmin)
xadmin.site.register(test_task,TaskAdmin)

