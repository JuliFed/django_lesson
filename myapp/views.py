from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskModelForm
from django.views.generic import TemplateView, View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView


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


class TasksView(View):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(request, 'myapp/index.html', {"tasks": tasks, "form": TaskModelForm(initial={'text': 'new'})})

    def post(self, request, pk=None):
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/tasks')
        else:
            tasks = Task.objects.all()
            return render(request, 'myapp/index.html', {"tasks": tasks, "form": form})


class TasksListView(ListView):
    model = Task
    template_name = 'myapp/index.html'
    context_object_name = 'tasks'
    # paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data()
        data["form"] = TaskModelForm()
        return data


class TaskDetailView(DetailView):
    model = Task
    template_name = 'myapp/task.html'

    # def get_object(self, queryset=None):
    #     obj = super().get_queryset(self.request)
    #     return obj

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data["form"] = TaskModelForm(instance=self.object)
        return data


class TaskFormView(FormView):
    form_class = TaskModelForm
    #для простых форм




