from django import forms
from django.contrib.auth.models import User
from items.models import Item

class ItemForm(forms.ModelForm):
    class Meta():
        model = Item
        fields = ('name','price', 'owner','condition', 'category','zipCode', 'picture')
