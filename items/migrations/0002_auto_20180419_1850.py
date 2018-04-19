# Generated by Django 2.0.3 on 2018-04-19 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('Appliances', 'Appliances'), ('Games', 'Games'), ('Arts, Crafts, & Sewing', 'Arts, Crafts, & Sewing'), ('Automotive Parts & Accessories', 'Automotive Parts & Accessories'), ('Baby & Baby Care', 'Baby & Baby Care'), ('Beauty & Personal Care', 'Beauty & Personal Care'), ('Books', 'Books'), ('CDs & Vinyl', 'CDs & Vinyl'), ('Cell Phones & Accessories', 'Cell Phones & Accessories'), ('Clothing', 'Clothing'), ('Shoes', 'Shoes'), ('Jewelry', 'Jewelry'), ('Collectibles', 'Collectibles'), ('Fine Art', 'Fine Art'), ('Computers', 'Computers'), ('Cources', 'Cources'), ('Credit & Payment Cards', 'Credit & Payment Cards'), ('Digital Music', 'Digital Music'), ('Electronics', 'Electronics'), ('Garden & Outdoor', 'Garden & Outdoor'), ('Gift Cards', 'Gift Cards'), ('Grocery & Gourmet Food', 'Grocery & Gourmet Food'), ('Handmade', 'Handmade'), ('Health', 'Health'), ('Household', 'Household'), ('Home & Business Services', 'Home & Business Services'), ('Home & Kitchen', 'Home & Kitchen'), ('Industrial & Scientific', 'Industrial & Scientific'), ('Luggage & Travel Gear', 'Luggage & Travel Gear'), ('Luxury Beatuty', 'Luxury Beatuty'), ('Magazine Subscriptions', 'Magazine Subscriptions'), ('Movies & TV', 'Movies & TV'), ('Musical Instruments', 'Musical Instruments'), ('Office Products', 'Office Products'), ('Pet Supplies', 'Pet Supplies'), ('Software', 'Software'), ('Sports & Outdoors', 'Sports & Outdoors'), ('Tools & Home Improvement', 'Tools & Home Improvement'), ('Toys & Games', 'Toys & Games'), ('Vehicles', 'Vehicles'), ('Video Games', 'Video Games')], max_length=30),
        ),
        migrations.AlterField(
            model_name='item',
            name='condition',
            field=models.CharField(choices=[('Bad', 'Bad'), ('Good', 'Good'), ('Excelllent', 'Excellent')], max_length=12),
        ),
    ]
