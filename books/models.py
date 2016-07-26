from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=200)
    shortdescription = models.CharField(max_length=500)
    timecreated = models.DateTimeField(auto_now=True)
