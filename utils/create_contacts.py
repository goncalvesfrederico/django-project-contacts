import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice
import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 1000

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False

django.setup()

if __name__ == "__main__":
    import faker
    from contact.models import Contact, Category

    # deleting all contacts and all category that exists in my tables, so if i don't want to delete the contacts and the categories i have, I just need to comment this lines bellow.
    Contact.objects.all().delete()
    Category.objects.all().delete()

    fake = faker.Faker("pt-BR")
    categories = ["Amigos", "Familia", "Conhecidos"]

    django_categories = [Category(name=name) for name in categories]

    for category in django_categories:
        category.save()

    django_contacts = []

    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        email = profile["mail"]
        first_name, last_name = profile['name'].split(' ', 1)
        phone = fake.phone_number()
        created_date: datetime = fake.date_this_year()
        description = fake.text(max_nb_chars=100)
        category = choice(django_categories)

        django_contacts.append(
            Contact(
                first_name = first_name,
                last_name = last_name,
                phone = phone,
                created_date = created_date,
                description = description,
                category = category,
            )
        )

    if len(django_contacts) > 0:
        Contact.objects.bulk_create(django_contacts)