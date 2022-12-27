from django import forms
from .models import employe
from django.forms import ModelForm

class empForm(forms.ModelForm):
    class Meta:
        model=employe
        fields='__all__'
