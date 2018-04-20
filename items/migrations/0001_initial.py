# Generated by Django 2.0.3 on 2018-04-19 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('condition', models.CharField(choices=[('New', 'New'), ('Bad', 'Bad'), ('Good', 'Good'), ('Excelllent', 'Excellent')], max_length=2)),
                ('category', models.CharField(choices=[('Appliances', 'Appliances'), ('Games', 'Games'), ('Arts, Crafts, & Sewing', 'Arts, Crafts, & Sewing'), ('Automotive Parts & Accessories', 'Automotive Parts & Accessories'), ('Baby & Baby Care', 'Baby & Baby Care'), ('Beauty & Personal Care', 'Beauty & Personal Care'), ('Books', 'Books'), ('CDs & Vinyl', 'CDs & Vinyl'), ('Cell Phones & Accessories', 'Cell Phones & Accessories'), ('Clothing', 'Clothing'), ('Shoes', 'Shoes'), ('Jewelry', 'Jewelry'), ('Collectibles', 'Collectibles'), ('Fine Art', 'Fine Art'), ('Computers', 'Computers'), ('Cources', 'Cources'), ('Credit & Payment Cards', 'Credit & Payment Cards'), ('Digital Music', 'Digital Music'), ('Electronics', 'Electronics'), ('Garden & Outdoor', 'Garden & Outdoor'), ('Gift Cards', 'Gift Cards'), ('Grocery & Gourmet Food', 'Grocery & Gourmet Food'), ('Handmade', 'Handmade'), ('Health', 'Health'), ('Household', 'Household'), ('Home & Business Services', 'Home & Business Services'), ('Home & Kitchen', 'Home & Kitchen'), ('Industrial & Scientific', 'Industrial & Scientific'), ('Luggage & Travel Gear', 'Luggage & Travel Gear'), ('Luxury Beatuty', 'Luxury Beatuty'), ('Magazine Subscriptions', 'Magazine Subscriptions'), ('Movies & TV', 'Movies & TV'), ('Musical Instruments', 'Musical Instruments'), ('Office Products', 'Office Products'), ('Pet Supplies', 'Pet Supplies'), ('Software', 'Software'), ('Sports & Outdoors', 'Sports & Outdoors'), ('Tools & Home Imporvement', 'Tools & Home Imporvement'), ('Toys & Games', 'Toys & Games'), ('Vehicles', 'Vehicles'), ('Video Games', 'Video Games')], max_length=2)),
                ('picture', models.ImageField(blank=True, upload_to='')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]