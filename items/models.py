from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    CONDITION_CHOICES = (
        ('Bad', 'Bad'),
        ('Good', 'Good'),
        ('Excellent', 'Excellent')
    )
    condition = models.CharField(choices=CONDITION_CHOICES,  max_length=12)
    CATEGORY_CHOICES = (
        ('Appliances', 'Appliances'),
        ('Games', 'Games'),
        ('Baby & Baby Care', 'Baby & Baby Care'),
        ('Books', 'Books'),
        ('CDs & Vinyl', 'CDs & Vinyl'),
        ('Cell Phones & Accessories', 'Cell Phones & Accessories'),
        ('Clothing', 'Clothing'),
        ('Shoes', 'Shoes'),
        ('Computers', 'Computers'),
        ('Electronics', 'Electronics'),
        ('Garden & Outdoor', 'Garden & Outdoor'),
        ('Handmade', 'Handmade'),
        ('Health', 'Health'),
        ('Household', 'Household'),
        ('Home & Kitchen', 'Home & Kitchen'),
        ('Industrial & Scientific', 'Industrial & Scientific'),
        ('Luggage & Travel Gear', 'Luggage & Travel Gear'),
        ('Musical Instruments', 'Musical Instruments'),
        ('Office Products', 'Office Products'),
        ('Pet Supplies', 'Pet Supplies'),
        ('Sports & Outdoors', 'Sports & Outdoors'),
        ('Tools & Home Improvement', 'Tools & Home Improvement'),
        ('Toys & Games', 'Toys & Games'),
        ('Vehicles', 'Vehicles'),
        ('Video Games', 'Video Games'),
    )
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=30)
    available = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='item_image')
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    zipCode = models.CharField(max_length=5, default='00000')
    description = models.TextField(max_length=150, default='')
    def get_absolute_url(self):
        return reverse("items:detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.name
