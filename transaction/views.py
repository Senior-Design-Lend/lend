from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from . import forms
from items.models import Item
from django.urls import reverse, reverse_lazy
# Create your views here.

class listTransactionView(ListView):
    context_object_name = 'transactions'
    template_name = 'transaction/index.html'
    model = models.Transaction
    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['active'] = models.Transaction.objects.filter(borrower=self.request.user, active=True)
        context['past'] = models.Transaction.objects.filter(borrower=self.request.user, active=False)
        return context

class detailRequestView(DetailView):
    model = models.Request
    context_object_name = 'request_detail'
    template = 'transaction/request_detail.html'

class createTransactionView(CreateView):
    model = models.Transaction
    form_class = forms.transactionForm
    def form_valid(self, form):
        transaction = form.save(commit=False)
        form.instance.owner = models.Request.objects.get(id=self.kwargs.get('pk')).requestee
        form.instance.borrower = self.request.user
        form.instance.item = models.Request.objects.get(id=self.kwargs.get('pk')).item
        form.instance.t_end = models.Request.objects.get(id=self.kwargs.get('pk')).end
        transaction.save()
        return super().form_valid(form)

class listRequestView(ListView):
    context_object_name = 'requests'
    template_name = 'transaction/requests.html'
    model = models.Request
    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['outgoing'] = models.Request.objects.filter(requester=self.request.user)
        context['incoming'] = models.Request.objects.filter(requestee=self.request.user)
        return context

class detailRequestView(DetailView):
    model = models.Request
    context_object_name = 'request_detail'
    template = 'transaction/request_detail.html'

class createRequestView(CreateView):
    model = models.Request
    form_class = forms.requestForm
    def form_valid(self, form):
        req = form.save(commit=False)
        form.instance.requester = self.request.user
        form.instance.requestee = Item.objects.get(id=self.kwargs.get('pk')).owner
        form.instance.item = Item.objects.get(id=self.kwargs.get('pk'))
        req.save()
        return super().form_valid(form)
