"""JUST URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from rest_framework import routers
from django.contrib.auth.models import User
from rest_framework.schemas import get_schema_view
from apps.casemanage import views
from django.views.static import serve
from JUST import settings

import xadmin
xadmin.autodiscover()

router=routers.DefaultRouter()

urlpatterns = [
    url(r'^$/', views.test_api),
    url(r'^admin/', xadmin.site.urls),
    url(r'^docs/', get_schema_view()),
    url(r'^api/getjson', views.test_api, name='test_api'),
    url(r'^api/read_log', views.read_log, name='read_log'),
    url(r'^api/set_serverip', views.set_serverip, name='set_serverip'),
    url(r'^api/get_newest_cases', views.get_newest_cases, name='get_newest_cases'),
    url(r'^admin/login_cool_css', views.login_cool_css, name="login_cool_css"),
    url(r'^showreport', views.showreport, name="showreport"),
    url(r'^reportfile/(?P<path>.*)$', serve, {'document_root': settings.REPORT_ROOT,'show_indexes': True}),
]
