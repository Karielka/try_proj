from django.urls import path

import quality_control.views as control

urlpatterns = [
    path('', control.index, name='index'),
    # path('bugs/', bug_list, name='bug_list'),
    # path('features/', feature_list, name='feature_list'),

    # # Параметризованные маршруты URL
    # path('bugs/<int:bug_id>/', bug_detail, name='bug_detail'),
    # path('features/<int:feature_id>/', feature_detail, name='feature_detail'),
]