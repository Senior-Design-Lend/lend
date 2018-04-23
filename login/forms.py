from django import forms
from django.contrib.auth.models import User
from login.models import UserProfileInfo
from django.core import validators


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('first_name', 'last_name','username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('interest1', 'interest2', 'interest3', 'city', 'state', 'profile_pic')
