from django.urls import path

import tasks.views as tasks

urlpatterns = [
    path('', tasks.index, name='index'),
    path('edit/<slug:task_pk>/', tasks.task_update, name='task-update'),
    path('delete/<slug:task_pk>/', tasks.task_delete, name='task-delete'),
]
