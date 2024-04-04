from django.urls import path

import quality_control.views as control

urlpatterns = [
    path('', control.index, name='index'),
    path('bugs/', control.bugs_read, name='bugs-read'),
    path('bugs/bug/<int:bug_id>/', control.bug_detail, name='bug-detail'),
    # path('features/', feature_list, name='feature_list'),

    # # Параметризованные маршруты URL
    
    # path('features/<int:feature_id>/', feature_detail, name='feature_detail'),
]