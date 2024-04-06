from django.urls import path

import quality_control.views as control

urlpatterns = [
    path('', control.index, name='index'),
    path('bugs/', control.bugs_read, name='bugs-read'),
    path('bugs/bug/<slug:bug_pk>/', control.bug_detail, name='bug-detail'),

    path('features/', control.features_read, name='features-read'),
    path('features/feature/<slug:feature_pk>/', control.feature_detail, name='feature-detail'),

    path('bug/create/', control.bug_create, name='bug-create'),
    path('feature/create/', control.feature_create, name='feature-create'),

    path('bug/edit/<slug:bug_pk>/', control.bug_update, name='bug-edit'),
    path('feature/edit/<slug:feature_pk>/', control.feature_update, name='feature-edit'),
    # path('features/', feature_list, name='feature_list'),

    # # Параметризованные маршруты URL
    
    # path('features/<int:feature_id>/', feature_detail, name='feature_detail'),
]