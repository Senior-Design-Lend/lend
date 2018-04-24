import os
import random
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'lendproject.settings')

import django
django.setup()

from login.models import User, Item
from faker import Faker
fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()
        fake_password = fakegen.password(length=10,special_chars=True, digits=True, lower_case=True)
        fake_rating = random.randint(100,500)/100
        fake_city = fakegen.city()
        fake_state = fakegen.state()
        user = User.objects.get_or_create(first_name=fake_first_name, last_name= fake_last_name, email=fake_email, password=fake_password, ratings=fake_rating, city=fake_city, state=fake_state)[0]
    for item in range(N):
        fake_item_name = fakegen.street_name()
        fake_item_price = random.randint(100,9999)/100
        fake_condition = 1
        item = Item.objects.get_or_create(name=fake_item_name, price=fake_item_price, condition=fake_condition, owner=user)


if __name__ == '__main__':
    print("Populating Database")
    populate(20)
