# Generated by Django 2.0.3 on 2018-04-23 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_auto_20180423_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]