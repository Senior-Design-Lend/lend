from django.shortcuts import render
from items.forms import ItemForm
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from django.urls import reverse, reverse_lazy

# Create your views here.
# class indexView(TemplateView):
#     template_name = 'items/index.html'
#

class listItemView(ListView):
    context_object_name = 'items'
    template_name = 'items/index.html'
    model = models.Item
    def get_queryset(self):
        return models.Item.objects.filter(owner=self.request.user)

class detailItemView(DetailView):
    model = models.Item
    context_object_name = 'item_detail'
    template_name = 'items/detailed.html'

class createItemView(CreateView):
    model = models.Item
    fields = ('name', 'price','condition', 'category', 'available','zipCode', 'picture')
    def form_valid(self, form):
        profile = form.save(commit=False)
        form.instance.owner = self.request.user
        profile.picture = form.cleaned_data['picture']
        profile.save()
        return super().form_valid(form)

class updateItemView(UpdateView):
    fields = ('name', 'price', 'condition', 'category', 'available', 'zipCode','picture')
    model = models.Item

class deleteItemView(DeleteView):
    model = models.Item
    success_url = reverse_lazy("items:list")
    template_name = 'items/delete.html'
