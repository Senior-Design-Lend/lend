from django.db import models

# Create your models here.
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
        ('Gift Cards', 'Gift Cards')
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
        ('Tools & Home Imporvement', 'Tools & Home Imporvement'),
        ('Toys & Games', 'Toys & Games'),
        ('Vehicles', 'Vehicles'),
        ('Video Games', 'Video Games'),
    )
    picture = models.ImageField(blank=True)

class Transaction(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
