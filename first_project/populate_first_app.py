# Needed imports
import os

# Configure settings
# It needs to run this before calling models from first_app
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
os.environ.update({"DJANGO_SETTINGS_MODULE": "first_project.settings"})


# Import settings
import django
django.setup()

from faker import Faker
from first_app.models import Topic, Webpage, AccessRecord
import random

# Fake population Script
fake_generator = Faker()
# List for random generator
topics = ["Search", "Social", "Marketplace", "News", "Games"]


def add_topic(topic):
    # get_or_create returns a tuple
    t = Topic.objects.get_or_create(top_name=topic)[0]
    t.save()
    return t


def add_webpage(topic_entry, url_entry, name_entry):
    web_page = Webpage.objects.get_or_create(
        topic=topic_entry, url=url_entry, name=name_entry)[0]
    web_page.save()
    return web_page


def add_acc_rec(webpage_name, date):
    acc_rec = AccessRecord.objects.get_or_create(
        name=webpage_name, date=date)[0]
    acc_rec.save()
    return acc_rec


def populate(N=5):
    '''
    Create N entries for all models 
    '''

    for entry in range(N):

        # Get topic for entry
        topic_choice = random.choice(topics)

        # Create fake data
        fake_url = fake_generator.url()
        fake_date = fake_generator.date()
        fake_name = fake_generator.company()

        # Create Topic entry
        topic = add_topic(topic_choice)

        # Create Webpage entry
        web_page = add_webpage(topic, fake_url, fake_name)

        # Create AccessRecord entry
        acc_rec = add_acc_rec(web_page, fake_date)


if __name__ == "__main__":
    print("Populating the database, please wait...")
    populate(20)
    print("Populating completed")
