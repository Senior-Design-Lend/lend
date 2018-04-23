from django import forms
from django.contrib.auth.models import User
from items.models import Item
from django.core import validators

class ItemForm(forms.ModelForm):
    class Meta():
        model = Item
        fields = ('name', 'price','condition', 'category', 'zipCode', 'available', 'picture')

    def clean(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError('prices can\'t be negative!')
