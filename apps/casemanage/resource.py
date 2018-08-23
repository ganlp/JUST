__author__ = 'Administrator'
##导入设置

from import_export import resources
from .models import  Case

class CaseResource(resources.ModelResource):
    class Meta:
        model=Case
        fields=('name','project','prepro','priority','proceduer','result','remark')
