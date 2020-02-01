import os
# Configure settings for project
# Need to run this before calling models from application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_two.settings')


import django
# Import settings
django.setup()

from faker import Faker
from app_two.models import Users
import random

generator = Faker()


def add_user(first_name, last_name, email):
    user = Users.objects.get_or_create(
        first_name=first_name, last_name=last_name, email=email)[0]
    user.save()
    return user


def populate(N=5):
    '''
    Create N entries for Users table
    '''
    for entry in range(N):
        # Generate fake data
        fake_first_name = generator.first_name()
        fake_last_name = generator.last_name()
        fake_email = generator.email()

        user = add_user(fake_first_name, fake_last_name, fake_email)


if __name__ == "__main__":
    print("Populating the database, please wait...")
    populate(30)
    print("Populating completed")
