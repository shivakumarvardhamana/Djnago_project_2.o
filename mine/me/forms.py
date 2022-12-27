

from django import forms
from django.contrib.auth.models import User
from .models import usercreate,user,login2

class userform(forms.ModelForm):

    class Meta:
        model=user
        fields='__all__'
        

class usercreateform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields='__all__'
       

class AuthenticationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=login2
        fields='__all__'



