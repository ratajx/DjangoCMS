# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-29 23:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0017_auto_20161230_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='short_text',
            field=models.TextField(max_length=200),
        ),
    ]
