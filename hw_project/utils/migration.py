import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw_project.settings")
django.setup()

from quotes.models import Quote, Author, Tag  # noqa

from .mongodb.connect import db

authors = db.authors.find()
for author in authors:
    print(author)
quotes = db.quotes.find()
