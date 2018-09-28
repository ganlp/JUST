from django.db import models
import sys
sys.path.append("../")
from testmanage.models import test_project

# Create your models here.
class Case(models.Model):
    pri_choice=(
        (1,'高'),
        (2,'中'),
        (3,'低'),
    )
    project=models.ForeignKey(test_project, on_delete=models.CASCADE,verbose_name='项目名称')
    name=models.CharField('用例名称',max_length=64)
    prepro=models.TextField('前置条件',max_length=128,blank=True)
    priority=models.IntegerField(choices=pri_choice,verbose_name='优先级',default=1)
    proceduer=models.TextField('测试步骤',max_length=256)
    result=models.TextField('预期结果',max_length=256)
    remark=models.TextField('备注',max_length=128,blank=True)


    def __str__(self):
        return self.name

    class Meta():
        verbose_name=u'测试用例'
        verbose_name_plural=u'测试用例'


class UIAuto(models.Model):
    project=models.ForeignKey(test_project, on_delete=models.CASCADE,verbose_name='项目名称')
    name=models.CharField('自动化版本名称',max_length=64)
    remark=models.TextField('备注',max_length=128,blank=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name=u'UI自动化'
        verbose_name_plural=u'UI自动化'

class ApiAuto(models.Model):
    project=models.ForeignKey(test_project, on_delete=models.CASCADE,verbose_name='项目名称')
    name=models.CharField('自动化版本名称',max_length=64)
    remark=models.TextField('备注',max_length=128,blank=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name=u'接口自动化'
        verbose_name_plural=u'接口自动化'


class Case_catagory(models.Model):
    upper_case = models.IntegerField(blank=True, null=True, verbose_name=u'上级分类ID')
    name = models.CharField(max_length=100, unique=True, verbose_name=u'分类名称')
    info = models.TextField(max_length=200, null=True, blank=True, verbose_name=u'分类说明')
    comment = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'备注')

    def __str__(self):
        return self.name

    class Meta():
        verbose_name=u'功能菜单'
        verbose_name_plural=u'功能菜单'
