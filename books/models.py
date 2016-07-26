from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=200)
    short_description = models.CharField(max_length=500)
    time_created = models.DateTimeField(auto_now=True)
