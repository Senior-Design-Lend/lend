from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=264, unique=True)
    password = models.CharField(max_length=264)
    ratings = models.DecimalField(max_digits=3, decimal_places=2)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=30)
    picture = models.ImageField(blank=True)

class Item(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    CONDITION_CHOICES = (
        ('New', 'New'),
        ('Bad', 'Bad'),
        ('Good', 'Good'),
        ('Excelllent', 'Excellent')
    )
    condition = models.CharField(choices=CONDITION_CHOICES,  max_length=2)
    picture = models.ImageField(blank=True)
