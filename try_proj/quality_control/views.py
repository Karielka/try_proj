from django.shortcuts import render, redirect, get_object_or_404
from quality_control.models import BugReport, FeatureReport

from django.http import HttpResponse
from quality_control.forms import BugReportFormForCreate, FeatureReportFormForCreate
from quality_control.forms import BugReportFormForEdit, FeatureReportFormForEdit

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

def bug_update(request, bug_pk):
    bug = get_object_or_404(BugReport, pk=bug_pk)
    form = BugReportFormForEdit(request.POST or None, instance=bug)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'quality_control/bug-edit.html', {'form': form})

def bug_delete(request, bug_pk=None):
    bug = get_object_or_404(BugReport, pk=bug_pk)
    if request.method == 'POST':
        bug.delete()
        return redirect('index')
    return render(request, 'quality_control/bug-delete.html', {'bug': bug})







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

def feature_update(request, feature_pk):
    feature = get_object_or_404(FeatureReport, pk=feature_pk)
    form = FeatureReportFormForEdit(request.POST or None, instance=feature)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'quality_control/feature-edit.html', {'form': form})

def feature_delete(request, feature_pk=None):
    feature = get_object_or_404(FeatureReport, pk=feature_pk)
    if request.method == 'POST':
        feature.delete()
        return redirect('index')
    return render(request, 'quality_control/feature-delete.html', {'feature': feature})