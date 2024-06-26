from django import forms
from quality_control.models import BugReport, FeatureReport

class BugReportFormForCreate(forms.ModelForm):
    class Meta:
        model = BugReport
        fields = ['title','description', 'profile', 'task', 'priority']

class FeatureReportFormForCreate(forms.ModelForm):
    class Meta:
        model = FeatureReport
        fields = ['title','description', 'profile', 'task', 'priority']

class BugReportFormForEdit(forms.ModelForm):
    class Meta:
        model = BugReport
        fields = ['description', 'priority', 'status']

class FeatureReportFormForEdit(forms.ModelForm):
    class Meta:
        model = FeatureReport
        fields = ['description', 'priority', 'status']