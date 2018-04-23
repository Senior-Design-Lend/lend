from django import forms
from django.contrib.auth.models import User
from . import models
from django.core import validators

class requestForm(forms.ModelForm):
    class Meta():
        model = models.Request
        fields = ('start', 'end')
    def clean(self):
        start = self.cleaned_data.get('start')
        end = self.cleaned_data.get('end')
        if end < start:
            raise forms.ValidationError('end time must be before start time')
