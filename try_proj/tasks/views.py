from django.shortcuts import render, redirect, get_object_or_404
from tasks.models import Profile, Task

from django.http import HttpResponse
from tasks.forms import TaskForm, TaskForm_1


def index(request):
    profiles = Profile.objects.all()
    context = {
        'title': 'Tasks Page',
        'message': 'Вы находитесь на страницами с заданиями для каждого профиля',
        'profiles': profiles,
        'page': 'main',
    }
    return render(request, 'tasks/index.html', context)

# def task_create(request, profile_pk):
#     profile = get_object_or_404(Profile, pk=profile_pk)
#     form = TaskForm(request.POST or None, instance=profile)
#     context = {
#         'profile': profile,
#         'page': 'create',
#         'form': form,
#     }
#     if form.is_valid():
#         form.save()
#         return redirect('index')
#     return render(request, 'tasks/task-create.html', context)

def task_create(request, profile_pk):
    profile = get_object_or_404(Profile, pk=profile_pk)
    if request.method == 'POST':
        form = TaskForm_1(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.profile = profile
            task.save()
            return redirect('index')  # Перенаправляем на главную страницу после создания задачи
    else:
        form = TaskForm_1()
    return render(request, 'tasks/task-create.html', {'form': form, 'profile_pk': profile_pk})



def task_read(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)
    context = {
        'task': task,
        'page': 'read',
    }
    return render(request, 'tasks/task-read.html', context)



# def task_update(request, task_pk=None):
#     task = Task.objects.get(pk=task_pk)
#     form = TaskForm(instance=task)
#     context = {
#         'task': task,
#         'form': form,
#     }
#     #print('------>', task)
#     return render(request, 'tasks/task-update.html', context)

def task_update(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'tasks/task-update.html', {'form': form})

def task_delete(request, task_pk=None):
    task = get_object_or_404(Task, pk=task_pk)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    return render(request, 'tasks/task-delete.html', {'task': task})