from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

class Book(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    published_date = models.DateField(
            blank=True, default=timezone.now)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    stock = models.IntegerField(default=0)

class Site(models.Model):
    name = models.CharField(max_length=50)
    only_log_in = models.BooleanField()
    content = models.TextField()