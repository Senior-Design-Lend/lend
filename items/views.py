from django.shortcuts import render
from items.forms import ItemForm
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.core import validators
from . import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class listItemView(ListView):
    context_object_name = 'items'
    template_name = 'items/index.html'
    model = models.Item

    def get_queryset(self):
        return models.Item.objects.filter(owner=self.request.user)

    def get_queryset(self):
        return models.Item.objects.filter(owner=self.request.user)


class detailItemView(DetailView):
    model = models.Item
    context_object_name = 'item_detail'
    template_name = 'items/detailed.html'

class createItemView(CreateView):
    model = models.Item
    form_class = forms.ItemForm
    def form_valid(self, form):
        profile = form.save(commit=False)
        form.instance.owner = self.request.user
        profile.picture = form.cleaned_data['picture']
        profile.save()
        return super().form_valid(form)


class updateItemView(UpdateView):
    form_class = forms.ItemForm
    model = models.Item
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != self.request.user:
            return HttpResponse("You are not allowed to edit this Post")
        return super(updateItemView, self).dispatch(request, *args, **kwargs)

class deleteItemView(DeleteView):
    model = models.Item
    success_url = reverse_lazy("items:list")
    template_name = 'items/delete.html'
    def delete(self, request, *args, **kwargs):
       obj = self.get_object()
       if obj.owner == request.user:
          self.object.delete()
          return HttpResponseRedirect(self.get_success_url())
       else:
           return HttpResponse('You can\'t Delete this item')
