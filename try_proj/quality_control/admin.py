from django.contrib import admin
from .models import BugReport, FeatureReport


@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    # Настройка отображения полей в списке объектов
    list_display = ('title', 'profile', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'priority')
    search_fields = ('title', 'description')
    
    # Настройка формы редактирования
    fieldsets = (
        ('Main', {
            'fields': ('title', 'description', 'profile', 'task', 'status', 'priority')
        }),
        ('Dates', {
            'fields': (),  # Пустой кортеж, чтобы исключить поля
            'classes': ('collapse',)
        }),
    )

    
    # Добавление пользовательского действия
    actions = ['mark_done']
    
    def mark_done(self, request, queryset):
        queryset.update(status='Done')
    mark_done.short_description = "Mark selected bug reports as done"

@admin.register(FeatureReport)
class FeatureReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'profile', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'priority')
    search_fields = ('title', 'description')
    # Настройка формы редактирования
    fieldsets = (
        ('Main', {
            'fields': ('title', 'description', 'profile', 'task', 'status', 'priority')
        }),
        ('Dates', {
            'fields': (),  # Пустой кортеж, чтобы исключить поля
            'classes': ('collapse',)
        }),
    )

