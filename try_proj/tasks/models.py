from django.db import models
#from django.contrib.auth.models import User 
#если конкретному пользователю необходимо назначать задание

class Profile(models.Model):
    title = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Профиль компании'
        verbose_name_plural = 'Профили компаний'

    def __str__(self):
        return self.title


class Task(models.Model):
    status_varient = [('New','Новая'),('In_work','В работе'),('Done','Завершена')]
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, related_name='tasks', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=status_varient, default='Новая',)

    def __str__(self):
        return f"Task title: { self.title }"
