from django.contrib import admin
import xadmin
from .models import Case,UIAuto,Case_catagory
from .resource import CaseResource
from .views import testView
from .xadmin_action import MyAction

from import_export.admin import ImportExportModelAdmin,ImportExportActionModelAdmin

# Register your models here.
class CaseAdmin(object):
    list_display = ['name','project','prepro','priority','proceduer','result','remark']
    search_fields = ['name','project__name']   #外键的查询必须指定查询字段
    list_filter = ['name','project__name']
    resource_class=CaseResource  ##导入设置
    import_export_args = {'import_resource_class': CaseResource, 'export_resource_class': CaseResource}
    model_icon='fa fa-lemon-o'
    refresh_times = (3, 5)

class UIAutoAdmin(object):
    list_display = ['id','project','name','remark',"go_to"]
    search_fields = ['name','project__name']   #外键的查询必须指定查询字段
    list_filter = ['name','project__name']
    model_icon='fa fa-lemon-o'
    actions=[MyAction,]

    def go_to(self,i):
        from django.utils.safestring import mark_safe
        return mark_safe("<a href=/admin/casemanage/test_view>详情</>")
    go_to.short_description = "详情"

class CatagoryAdmin(object):
    list_display=['id','name','info']
    search_fields = ['name']

xadmin.site.register(Case,CaseAdmin)
xadmin.site.register(UIAuto,UIAutoAdmin)
xadmin.site.register(Case_catagory,CatagoryAdmin)
xadmin.site.register_view(r'test_view/',testView,name='for_test')