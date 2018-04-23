from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from items.models import Item
from login.models import UserProfileInfo
import random
import pdb

class homeView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = self.getItems()
        if self.request.user.is_authenticated:
            context['userItems'] = self.getUserItems()
            context['userProfile'] = self.getUserProfileInfo()
            context['in1Items'] = self.getRelevantItems(context['userProfile'].interest1)
            context['in2Items'] = self.getRelevantItems(context['userProfile'].interest2)
            context['in3Items'] = self.getRelevantItems(context['userProfile'].interest3)
        return context

    def getItems(self):
        allItems = Item.objects.all()
        return allItems

    def getUserItems(self):
        userItems = Item.objects.filter(owner=self.request.user).order_by('-update_date')
        return userItems

    def getUserProfileInfo(self):
        userProfileInfo = UserProfileInfo.objects.filter(user=self.request.user)
        return userProfileInfo[0]
       
    def getRelevantItems(self, interest):
        interestItems = Item.objects.filter(category=interest)
        randomNums = random.sample(range(0,interestItems.count()), 5)
        itemsList = []
        for i in randomNums:
            itemsList.append(interestItems[i])
        return itemsList
    