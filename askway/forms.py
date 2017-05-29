import re
from django import forms
from django.contrib.auth.models import User
from .models import *
from django.core.exceptions import ObjectDoesNotExist

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password',widget=forms.PasswordInput())

class AnsForm(forms.Form):
	answer = forms.CharField(label='Answer', max_length=500)

class QuesForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ['question']
        exclude = ['post_by']

class SignupForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput())
    password2 = forms.CharField(label='Re-Enter Password',widget=forms.PasswordInput())