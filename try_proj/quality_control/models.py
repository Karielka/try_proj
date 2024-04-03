from django.db import models
from tasks.models import Profile, Task

class BaseReport(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    priority = models.PositiveIntegerField(choices=[(i, i) for i in range(6)], default=0)

    # Times
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class BugReport(BaseReport):
    STATUS_CHOICES = [('New', 'Новая'), ('In_work', 'В работе'), ('Done', 'Завершена')]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')

    class Meta:
        verbose_name = 'Баг-репорт'
        verbose_name_plural = 'Баг-репорты'

    def __str__(self):
        return self.title

class FeatureReport(BaseReport):
    STATUS_CHOICES = [('Reviewed', 'Рассмотрено'), ('Accepted', 'Принято'), ('Rejected', 'Отклонено')]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Reviewed')

    class Meta:
        verbose_name = 'Фича-репорт'
        verbose_name_plural = 'Фича-репорты'

    def __str__(self):
        return self.title
