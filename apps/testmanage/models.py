from __future__ import unicode_literals

from django.db import models
import django.utils.timezone as timezone
from django.contrib.auth.models import User
# Create your models here.
class test_project(models.Model):
    name=models.CharField('项目名称',max_length=64)
    start_time= models.DateTimeField('开始时间',default=timezone.now) #auto_now=True
    create_person=models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='责任人')

    def __str__(self):
        return self.name

    class Meta():
        verbose_name=u'项目管理'
        verbose_name_plural=u'项目管理'

class test_version(models.Model):
    project=models.ForeignKey(test_project,verbose_name='项目名称',on_delete=models.CASCADE)
    name=models.CharField('版本名称',max_length=64)
    status = models.BooleanField('状态')
    start_time=models.DateTimeField('开始时间',default=timezone.now)
    create_person=models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='责任人')
    desc=models.CharField('描述',max_length=256)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name=u'版本管理'
        verbose_name_plural=u'版本管理'
        unique_together=('project','name')

class test_task(models.Model):
#    project=models.ForeignKey(test_project,verbose_name='项目名称',on_delete=models.CASCADE)
    status_choice=(
        (1,'未开始'),
        (2,'进行中'),
        (3,'阻塞'),
        (4,'完成')
    )
    version=models.ForeignKey(test_version,verbose_name='版本名称',on_delete=models.CASCADE)
    name=models.CharField('任务名称',max_length=64)
    start_time=models.DateTimeField('开始时间',auto_now=True)
    res_person=models.ManyToManyField(User,verbose_name='参与者', blank=True)
    status=models.IntegerField(choices=status_choice,default=1,verbose_name='状态')
 #   attend_person=models.ManyToManyField(User,verbose_name='参与者', blank=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name=u'任务管理'
        verbose_name_plural=u'任务管理'
        unique_together=('version','name')


