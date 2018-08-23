__author__ = 'Administrator'

from django.http import HttpResponse
from xadmin.plugins.actions import BaseActionView

class MyAction(BaseActionView):
    action_name = "change_css"
    description = u'Test selected %(verbose_name_plural)s'
    model_perm = 'change'
    def do_action(self, queryset):
        for obj in queryset:
            obj.remark += 'sss'
            obj.save()
            return HttpResponse('{"status": "success", "msg": "error"}', content_type='application/json')