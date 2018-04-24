from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    CATEGORY_CHOICES = (
        ('None', 'None'),
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
    STATES = (('AL', 'AL'), ('AK', 'AK'), ('AZ', 'AZ'), ('AR', 'AR'), ('CA', 'CA'), ('CO', 'CO'), ('CT', 'CT'), ('DC', 'DC'), ('DE', 'DE'),
     ('FL', 'FL'), ('GA', 'GA'), ('HI', 'HI'), ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN'), ('IA', 'IA'), ('KS', 'KS'), ('KY', 'KY'), ('LA', 'LA'),
     ('ME', 'ME'), ('MD', 'MD'), ('MA', 'MA'), ('MI', 'MI'), ('MN', 'MN'), ('MS', 'MS'), ('MO', 'MO'), ('MT', 'MT'), ('NE', 'NE'), ('NV', 'NV'),
      ('NH', 'NH'), ('NJ', 'NJ'), ('NM', 'NM'), ('NY', 'NY'), ('NC', 'NC'), ('ND', 'ND'), ('OH', 'OH'), ('OK', 'OK'), ('OR', 'OR'), ('PA', 'PA'),
      ('RI', 'RI'), ('SC', 'SC'), ('SD', 'SD'), ('TN', 'TN'), ('TX', 'TX'), ('UT', 'UT'), ('VT', 'VT'), ('VA', 'VA'), ('WA', 'WA'), ('WV', 'WV'),
      ('WI', 'WI'), ('WY', 'WY'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interest1 = models.CharField(choices=CATEGORY_CHOICES, max_length=30, default='None')
    interest2 = models.CharField(choices=CATEGORY_CHOICES, max_length=30, default='None')
    interest3 = models.CharField(choices=CATEGORY_CHOICES, max_length=30, default='None')
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(choices=STATES, max_length=30, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)
    def __str__(self):
        return self.user.username
