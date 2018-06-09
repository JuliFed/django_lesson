from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, 'myapp/index.html', {"tasks": tasks})
    # return HttpResponse('Hello world!')


def create_task(request):
    if request.method == 'POST':
        task = Task(text=request.POST.get('text'), checked=request.POST.get('checked', False))
        task.save()
    return redirect('/tasks')

