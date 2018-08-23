# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
#from suit.apps import DjangoSuitConfig
'''
class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
'''
class TestmanageConfig(AppConfig):
    name = 'testmanage'

class MyappConfig(AppConfig):
    name="testmanage"
    verbose_name="基础数据管理"