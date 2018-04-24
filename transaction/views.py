from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from . import forms
from items.models import Item
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def endTransaction(request, id):
    transaction = models.Transaction.objects.get(id=id)
    transaction.active = False
    transaction.save()
    return HttpResponseRedirect(reverse('transaction:list'))

class listTransactionView(ListView):
    context_object_name = 'transactions'
    template_name = 'transaction/index.html'
    model = models.Transaction
    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['active'] = models.Transaction.objects.filter(Q(borrower=self.request.user) | Q(owner=self.request.user), active=True)
        context['past'] = models.Transaction.objects.filter(Q(borrower=self.request.user) | Q(owner=self.request.user), active=False)
        return context

class detailTransactionView(DetailView):
    model = models.Transaction
    context_object_name = 'transaction_detail'
    template = 'transaction/transaction_detail.html'

class createTransactionView(CreateView):
    model = models.Transaction
    form_class = forms.transactionForm
    def form_valid(self, form):
        transaction = form.save(commit=False)
        form.instance.owner = models.Request.objects.get(id=self.kwargs.get('pk')).requestee
        form.instance.borrower = models.Request.objects.get(id=self.kwargs.get('pk')).requester
        form.instance.item = models.Request.objects.get(id=self.kwargs.get('pk')).item
        form.instance.t_end = models.Request.objects.get(id=self.kwargs.get('pk')).end
        transaction.save()
        models.Request.objects.get(id=self.kwargs.get('pk')).delete()
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
