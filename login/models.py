from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ratings = models.DecimalField(max_digits=3, decimal_places=2, default='0')
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=30, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)
    def __str__(self):
        return self.user.username


# class Item(models.Model):
#     name = models.CharField(max_length=128)
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     CONDITION_CHOICES = (
#         ('New', 'New'),
#         ('Bad', 'Bad'),
#         ('Good', 'Good'),
#         ('Excelllent', 'Excellent')
#     )
#     condition = models.CharField(choices=CONDITION_CHOICES,  max_length=2)
#     picture = models.ImageField(blank=True)
