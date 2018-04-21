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
        ('Excelllent', 'Excellent')
    )
    condition = models.CharField(choices=CONDITION_CHOICES,  max_length=12)
    CATEGORY_CHOICES = (
        ('Appliances', 'Appliances'),
        ('Games', 'Games'),
        ('Arts, Crafts, & Sewing', 'Arts, Crafts, & Sewing'),
        ('Automotive Parts & Accessories', 'Automotive Parts & Accessories'),
        ('Baby & Baby Care', 'Baby & Baby Care'),
        ('Beauty & Personal Care', 'Beauty & Personal Care'),
        ('Books', 'Books'),
        ('CDs & Vinyl', 'CDs & Vinyl'),
        ('Cell Phones & Accessories', 'Cell Phones & Accessories'),
        ('Clothing', 'Clothing'),
        ('Shoes', 'Shoes'),
        ('Jewelry', 'Jewelry'),
        ('Collectibles', 'Collectibles'),
        ('Fine Art', 'Fine Art'),
        ('Computers', 'Computers'),
        ('Cources', 'Cources'),
        ('Credit & Payment Cards', 'Credit & Payment Cards'),
        ('Digital Music', 'Digital Music'),
        ('Electronics', 'Electronics'),
        ('Garden & Outdoor', 'Garden & Outdoor'),
        ('Gift Cards', 'Gift Cards'),
        ('Grocery & Gourmet Food', 'Grocery & Gourmet Food'),
        ('Handmade', 'Handmade'),
        ('Health', 'Health'),
        ('Household', 'Household'),
        ('Home & Business Services', 'Home & Business Services'),
        ('Home & Kitchen', 'Home & Kitchen'),
        ('Industrial & Scientific', 'Industrial & Scientific'),
        ('Luggage & Travel Gear', 'Luggage & Travel Gear'),
        ('Luxury Beatuty', 'Luxury Beatuty'),
        ('Magazine Subscriptions', 'Magazine Subscriptions'),
        ('Movies & TV', 'Movies & TV'),
        ('Musical Instruments', 'Musical Instruments'),
        ('Office Products', 'Office Products'),
        ('Pet Supplies', 'Pet Supplies'),
        ('Software', 'Software'),
        ('Sports & Outdoors', 'Sports & Outdoors'),
        ('Tools & Home Improvement', 'Tools & Home Improvement'),
        ('Toys & Games', 'Toys & Games'),
        ('Vehicles', 'Vehicles'),
        ('Video Games', 'Video Games'),
    )
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=30)
    available = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='item_image',blank=True)

    def get_absolute_url(self):
        return reverse("items:detail", kwargs={'pk':self.pk})
        
    def __str__(self):
        return self.name
