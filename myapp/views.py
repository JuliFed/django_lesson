from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskModelForm


def index(request):
    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('OK')
            return redirect('/tasks')
        else:
            tasks = Task.objects.all()
            return render(request, 'myapp/index.html', {"tasks": tasks, "form": form})

    tasks = Task.objects.all()
    return render(request, 'myapp/index.html', {"tasks": tasks, "form": TaskModelForm(initial={'text': 'new'})})


def detail_task(request, pk):
    try:
        task = Task.objects.get(id=pk)
        if request.method == 'POST':
            form = TaskModelForm(request.POST, instance=task)
            if form.is_valid():
                form.save(commit=True)
                return redirect('/tasks/{}/'.format(task.pk))
            else:
                return render(request, 'myapp/task.html', {"task": task, 'form': form})

        form = TaskModelForm(instance=task)
        return render(request, 'myapp/task.html', {"task": task, 'form': form})
    except Task.DoesNotExist:
        return HttpResponse(status=404)
