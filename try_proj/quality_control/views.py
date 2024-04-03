from django.shortcuts import render

def index(request):
    return render(request, 'quality_control/index.html', {'title': 'Система контроля качества'})

# def bug_list(request):
#     return render(request, 'quality_control/bug_list.html', {'title': 'Список отчетов об ошибках'})

# def feature_list(request):
#     return render(request, 'quality_control/feature_list.html', {'title': 'Список запросов на улучшение'})

# def bug_detail(request, bug_id):
#     return render(request, 'quality_control/bug_detail.html', {'title': f'Детали бага {bug_id}'})

# def feature_detail(request, feature_id):
#     return render(request, 'quality_control/feature_detail.html', {'title': f'Детали улучшения {feature_id}'})
