from django import forms
from.models import Task
from django.forms import ModelForm

class TaskForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new'}))
    class Meta:
        model=Task
        fields='__all__'

class updateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields='__all__'