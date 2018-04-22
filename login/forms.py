from django import forms
from django.contrib.auth.models import User
from login.models import UserProfileInfo
from django.core import validators


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('first_name', 'last_name','username', 'email', 'password')
    def clean(self):
        password = self.cleaned_data.get('password')
        vpassword = self.cleaned_data.get('vpassword')

        if password != vpassword:
            raise forms.ValidationError('passwords must match!')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('interest1', 'interest2', 'interest3', 'city', 'state', 'profile_pic')
