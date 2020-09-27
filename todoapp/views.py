from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.

def index(request):
    task_list = Task.objects.all()
    output = ','.join([q.task_name for q in task_list])
    return HttpResponse(output)






