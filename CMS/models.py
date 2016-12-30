from __future__ import unicode_literals
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Site(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    main_header_of_site = models.CharField(max_length=200, default='', blank=True)
    content = RichTextUploadingField()
    enable = models.BooleanField(default=True)
    only_for_log_in = models.BooleanField()

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=100, blank=False)
    short_text = models.TextField(max_length=200)
    full_text = RichTextUploadingField()
    enable = models.BooleanField(default=True)
    date = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    date = models.DateTimeField(default=timezone.now, editable=False)
    comment = models.TextField(max_length=3000, editable=False)
    news = models.ForeignKey(News, on_delete=models.CASCADE, editable=False, null=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, editable=False, null=True)


class Logo(models.Model):
    logo = models.ImageField(null=True)

    def __str__(self):
        if self.logo.name is not None:
            return self.logo.name
        else:
            return 'not set'
