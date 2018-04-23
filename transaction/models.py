from django.db import models
from django.contrib.auth.models import User
from items.models import Item
from datetime import date
from django.urls import reverse


# Create your models here.
class Transaction(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrower')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    t_start = models.DateField(auto_now_add=True)
    t_end = models.DateField()
    active = models.BooleanField(default=True)
    def get_absolute_url(self):
        return reverse("postman:write", kwargs={'recipients':Request.objects.get(id=self.pk).requestee})

class Request(models.Model):
    requestee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requestee')
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requester')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    start = models.DateField(default=date.today)
    end = models.DateField(default=date.today)

    def get_absolute_url(self):
        return reverse("postman:write", kwargs={'recipients':Request.objects.get(id=self.pk).requestee})
        # return reverse("postman:write")
