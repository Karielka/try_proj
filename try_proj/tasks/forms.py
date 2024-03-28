from django import forms
from tasks.models import Task, Profile

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

class TaskForm_1(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'