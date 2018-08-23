from django.shortcuts import render
from .models import  test_task,test_project,test_version

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
import bootstrap3
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render,get_object_or_404
from xadmin.views import BaseAdminView

# Create your views here.
def index(request):
	return HttpResponse("Hello Django!")
#	return render(request, "test.html")

