# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-28 15:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0004_auto_20161228_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='content',
        ),
    ]