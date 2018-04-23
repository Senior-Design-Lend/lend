from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from items.models import Item
import pdb

class homeView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = self.getItems()
        if self.request.user.is_authenticated:
            context['userItems'] = self.getUserItems()
        return context

    def getItems(self):
        allItems = Item.objects.all()
        return allItems

    def getUserItems(self):
        userItems = Item.objects.filter(owner=self.request.user)
        return userItems
