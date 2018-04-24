from django.shortcuts import render
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from login.models import UserProfileInfo
from django.contrib.auth.models import User

from items.models import Item
class profileView(TemplateView):
    template_name = "profile/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        ownerID = User.objects.get(id=self.kwargs['pk'])
        context['items'] = Item.objects.filter(owner=ownerID)
        context['picture'] = UserProfileInfo.objects.get(user=ownerID).profile_pic
        context['first'] = User.objects.get(id=self.kwargs['pk']).first_name
        context['last'] = User.objects.get(id=self.kwargs['pk']).last_name


        return context

    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)
