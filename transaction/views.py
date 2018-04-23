from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from django.urls import reverse, reverse_lazy
# Create your views here.

class listTransactionView(ListView):
    context_object_name = 'transactions'
    template_name = 'transaction/index.html'
    model = models.Transaction