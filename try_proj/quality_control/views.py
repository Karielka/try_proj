from django.shortcuts import render, redirect, get_object_or_404
from quality_control.models import BugReport, FeatureReport

from django.http import HttpResponse
from quality_control.forms import BugReportFormForCreate, FeatureReportFormForCreate

def index(request):
    bugs = BugReport.objects.all()
    features = FeatureReport.objects.all()
    context = {
        'title': 'Report Page',
        'message': 'Вы находитесь на страницами со списком фич и багов',
        'bugs': bugs,
        'features': features,
        'page': 'main',
    }
    return render(request, 'quality_control/index.html', context)

def bugs_read(request):
    bugs = BugReport.objects.all()
    context = {
        'title': 'Bugs page',
        'message': 'Вы находитесь на страницами со списком багов',
        'bugs': bugs,
    }
    return render(request, 'quality_control/bugs-read.html', context)

def bug_detail(request, bug_pk):
    bug = get_object_or_404(BugReport, pk=bug_pk)
    context = {
        'title': 'Bug page',
        'message': 'Вы находитесь на страницами с конкретным багом',
        'bug': bug,
    }
    return render(request, 'quality_control/bug-read.html', context)


def bug_create(request):
    if request.method == 'POST':
        form = BugReportFormForCreate(request.POST)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.save()
            return redirect('index')  # Перенаправляем на главную страницу после создания
    else:
        form = BugReportFormForCreate()
    context = {
        'title': 'Feature page create',
        'message': 'Вы находитесь на страницами с созданием конкретного бага',
        'form': form,
    }
    return render(request, 'quality_control/bug-create.html', context)











def features_read(request):
    features = FeatureReport.objects.all()
    context = {
        'title': 'Features page',
        'message': 'Вы находитесь на страницами со списком фич',
        'features': features,
    }
    return render(request, 'quality_control/features-read.html', context)

def feature_detail(request, feature_pk):
    feature = get_object_or_404(FeatureReport, pk=feature_pk)
    context = {
        'title': 'Feature page',
        'message': 'Вы находитесь на страницами с конкретной фичей',
        'feature': feature,
    }
    return render(request, 'quality_control/feature-read.html', context)

def feature_create(request):
    if request.method == 'POST':
        form = FeatureReportFormForCreate(request.POST)
        if form.is_valid():
            feature = form.save(commit=False)
            feature.save()
            return redirect('index')  # Перенаправляем на главную страницу после создания
    else:
        form = FeatureReportFormForCreate()
    context = {
        'title': 'Feature page create',
        'message': 'Вы находитесь на страницами с созданием конкретного бага',
        'form': form,
    }
    return render(request, 'quality_control/feature-create.html', context)


# def task_create(request, profile_pk):
#     profile = get_object_or_404(Profile, pk=profile_pk)
#     if request.method == 'POST':
#         form = TaskForm_1(request.POST)
#         if form.is_valid():
#             task = form.save(commit=False)
#             task.profile = profile
#             task.save()
#             return redirect('index')  # Перенаправляем на главную страницу после создания задачи
#     else:
#         form = TaskForm_1()
#     context = {
#         'form': form,
#         'profile_pk': profile_pk,
#         'message': "Вы создаёте задание",
#         'page': 'create',
#     }
#     return render(request, 'tasks/task-create.html', context)

# def task_read(request, task_pk):
#     task = get_object_or_404(Task, pk=task_pk)
#     context = {
#         'task': task,
#         'page': 'read',
#         'message': "Вы читаете задание",
#         'page': 'read',
#     }
#     return render(request, 'tasks/task-read.html', context)

# def task_update(request, task_pk):
#     task = get_object_or_404(Task, pk=task_pk)
#     form = TaskForm(request.POST or None, instance=task)
#     if form.is_valid():
#         form.save()
#         return redirect('index')
#     return render(request, 'tasks/task-update.html', {'form': form})

# def task_delete(request, task_pk=None):
#     task = get_object_or_404(Task, pk=task_pk)
#     if request.method == 'POST':
#         task.delete()
#         return redirect('index')
#     return render(request, 'tasks/task-delete.html', {'task': task})