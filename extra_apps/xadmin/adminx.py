from __future__ import absolute_import
import xadmin
from .models import UserSettings, Log
from django.contrib import admin

from xadmin.layout import *

from django.utils.translation import ugettext_lazy as _, ugettext

from xadmin import views

#######add主题配置
class BaseSetging(object):
    enable_themes=True
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView,BaseSetging)
############

class GlobalSetting(object):
    site_title = u"自动化测试管理平台"
    site_footer = u"author@ganlp版权所有"
    menu_style="accordion"
    # global_search_models=[V_UserInfo,UserDistrict]
    # global_models_icon={
    #     V_UserInfo:"glyphicon glyphicon-user",UserDistrict:"fa fa-cloud"
    # }
xadmin.site.register(views.CommAdminView, GlobalSetting)

class UserSettingsAdmin(object):
    model_icon = 'fa fa-cog'
    hidden_menu = True

xadmin.site.register(UserSettings, UserSettingsAdmin)

class LogAdmin(object):

    def link(self, instance):
        if instance.content_type and instance.object_id and instance.action_flag != 'delete':
            admin_url = self.get_admin_url('%s_%s_change' % (instance.content_type.app_label, instance.content_type.model), 
                instance.object_id)
            return "<a href='%s'>%s</a>" % (admin_url, _('Admin Object'))
        else:
            return ''
    link.short_description = ""
    link.allow_tags = True
    link.is_column = False

    list_display = ('action_time', 'user', 'ip_addr', '__str__', 'link')
    list_filter = ['user', 'action_time']
    search_fields = ['ip_addr', 'message']
    model_icon = 'fa fa-cog'


class UserInfAdmin(object):
    pass

xadmin.site.register(Log, LogAdmin)


