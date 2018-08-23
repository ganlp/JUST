#-*-coding:utf-8-*-
__author__ = 'Administrator'


from ..models import Case_catagory
from django import template
register = template.Library()
@register.filter(name='getNextCatagory')
def getNextCatagory(value):
    return Case_catagory.objects.filter(upper_case = value)
