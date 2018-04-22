# Generated by Django 2.0.3 on 2018-04-22 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20180409_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='interest1',
            field=models.CharField(choices=[('None', 'None'), ('Appliances', 'Appliances'), ('Games', 'Games'), ('Arts, Crafts, & Sewing', 'Arts, Crafts, & Sewing'), ('Automotive Parts & Accessories', 'Automotive Parts & Accessories'), ('Baby & Baby Care', 'Baby & Baby Care'), ('Beauty & Personal Care', 'Beauty & Personal Care'), ('Books', 'Books'), ('CDs & Vinyl', 'CDs & Vinyl'), ('Cell Phones & Accessories', 'Cell Phones & Accessories'), ('Clothing', 'Clothing'), ('Shoes', 'Shoes'), ('Jewelry', 'Jewelry'), ('Collectibles', 'Collectibles'), ('Fine Art', 'Fine Art'), ('Computers', 'Computers'), ('Cources', 'Cources'), ('Credit & Payment Cards', 'Credit & Payment Cards'), ('Digital Music', 'Digital Music'), ('Electronics', 'Electronics'), ('Garden & Outdoor', 'Garden & Outdoor'), ('Gift Cards', 'Gift Cards'), ('Grocery & Gourmet Food', 'Grocery & Gourmet Food'), ('Handmade', 'Handmade'), ('Health', 'Health'), ('Household', 'Household'), ('Home & Business Services', 'Home & Business Services'), ('Home & Kitchen', 'Home & Kitchen'), ('Industrial & Scientific', 'Industrial & Scientific'), ('Luggage & Travel Gear', 'Luggage & Travel Gear'), ('Luxury Beatuty', 'Luxury Beatuty'), ('Magazine Subscriptions', 'Magazine Subscriptions'), ('Movies & TV', 'Movies & TV'), ('Musical Instruments', 'Musical Instruments'), ('Office Products', 'Office Products'), ('Pet Supplies', 'Pet Supplies'), ('Software', 'Software'), ('Sports & Outdoors', 'Sports & Outdoors'), ('Tools & Home Improvement', 'Tools & Home Improvement'), ('Toys & Games', 'Toys & Games'), ('Vehicles', 'Vehicles'), ('Video Games', 'Video Games')], default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='interest2',
            field=models.CharField(choices=[('None', 'None'), ('Appliances', 'Appliances'), ('Games', 'Games'), ('Arts, Crafts, & Sewing', 'Arts, Crafts, & Sewing'), ('Automotive Parts & Accessories', 'Automotive Parts & Accessories'), ('Baby & Baby Care', 'Baby & Baby Care'), ('Beauty & Personal Care', 'Beauty & Personal Care'), ('Books', 'Books'), ('CDs & Vinyl', 'CDs & Vinyl'), ('Cell Phones & Accessories', 'Cell Phones & Accessories'), ('Clothing', 'Clothing'), ('Shoes', 'Shoes'), ('Jewelry', 'Jewelry'), ('Collectibles', 'Collectibles'), ('Fine Art', 'Fine Art'), ('Computers', 'Computers'), ('Cources', 'Cources'), ('Credit & Payment Cards', 'Credit & Payment Cards'), ('Digital Music', 'Digital Music'), ('Electronics', 'Electronics'), ('Garden & Outdoor', 'Garden & Outdoor'), ('Gift Cards', 'Gift Cards'), ('Grocery & Gourmet Food', 'Grocery & Gourmet Food'), ('Handmade', 'Handmade'), ('Health', 'Health'), ('Household', 'Household'), ('Home & Business Services', 'Home & Business Services'), ('Home & Kitchen', 'Home & Kitchen'), ('Industrial & Scientific', 'Industrial & Scientific'), ('Luggage & Travel Gear', 'Luggage & Travel Gear'), ('Luxury Beatuty', 'Luxury Beatuty'), ('Magazine Subscriptions', 'Magazine Subscriptions'), ('Movies & TV', 'Movies & TV'), ('Musical Instruments', 'Musical Instruments'), ('Office Products', 'Office Products'), ('Pet Supplies', 'Pet Supplies'), ('Software', 'Software'), ('Sports & Outdoors', 'Sports & Outdoors'), ('Tools & Home Improvement', 'Tools & Home Improvement'), ('Toys & Games', 'Toys & Games'), ('Vehicles', 'Vehicles'), ('Video Games', 'Video Games')], default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='interest3',
            field=models.CharField(choices=[('None', 'None'), ('Appliances', 'Appliances'), ('Games', 'Games'), ('Arts, Crafts, & Sewing', 'Arts, Crafts, & Sewing'), ('Automotive Parts & Accessories', 'Automotive Parts & Accessories'), ('Baby & Baby Care', 'Baby & Baby Care'), ('Beauty & Personal Care', 'Beauty & Personal Care'), ('Books', 'Books'), ('CDs & Vinyl', 'CDs & Vinyl'), ('Cell Phones & Accessories', 'Cell Phones & Accessories'), ('Clothing', 'Clothing'), ('Shoes', 'Shoes'), ('Jewelry', 'Jewelry'), ('Collectibles', 'Collectibles'), ('Fine Art', 'Fine Art'), ('Computers', 'Computers'), ('Cources', 'Cources'), ('Credit & Payment Cards', 'Credit & Payment Cards'), ('Digital Music', 'Digital Music'), ('Electronics', 'Electronics'), ('Garden & Outdoor', 'Garden & Outdoor'), ('Gift Cards', 'Gift Cards'), ('Grocery & Gourmet Food', 'Grocery & Gourmet Food'), ('Handmade', 'Handmade'), ('Health', 'Health'), ('Household', 'Household'), ('Home & Business Services', 'Home & Business Services'), ('Home & Kitchen', 'Home & Kitchen'), ('Industrial & Scientific', 'Industrial & Scientific'), ('Luggage & Travel Gear', 'Luggage & Travel Gear'), ('Luxury Beatuty', 'Luxury Beatuty'), ('Magazine Subscriptions', 'Magazine Subscriptions'), ('Movies & TV', 'Movies & TV'), ('Musical Instruments', 'Musical Instruments'), ('Office Products', 'Office Products'), ('Pet Supplies', 'Pet Supplies'), ('Software', 'Software'), ('Sports & Outdoors', 'Sports & Outdoors'), ('Tools & Home Improvement', 'Tools & Home Improvement'), ('Toys & Games', 'Toys & Games'), ('Vehicles', 'Vehicles'), ('Video Games', 'Video Games')], default='None', max_length=30),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='state',
            field=models.CharField(blank=True, choices=[('AL', 'AL'), ('AK', 'AK'), ('AZ', 'AZ'), ('AR', 'AR'), ('CA', 'CA'), ('CO', 'CO'), ('CT', 'CT'), ('DC', 'DC'), ('DE', 'DE'), ('FL', 'FL'), ('GA', 'GA'), ('HI', 'HI'), ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN'), ('IA', 'IA'), ('KS', 'KS'), ('KY', 'KY'), ('LA', 'LA'), ('ME', 'ME'), ('MD', 'MD'), ('MA', 'MA'), ('MI', 'MI'), ('MN', 'MN'), ('MS', 'MS'), ('MO', 'MO'), ('MT', 'MT'), ('NE', 'NE'), ('NV', 'NV'), ('NH', 'NH'), ('NJ', 'NJ'), ('NM', 'NM'), ('NY', 'NY'), ('NC', 'NC'), ('ND', 'ND'), ('OH', 'OH'), ('OK', 'OK'), ('OR', 'OR'), ('PA', 'PA'), ('RI', 'RI'), ('SC', 'SC'), ('SD', 'SD'), ('TN', 'TN'), ('TX', 'TX'), ('UT', 'UT'), ('VT', 'VT'), ('VA', 'VA'), ('WA', 'WA'), ('WV', 'WV')], max_length=30),
        ),
    ]