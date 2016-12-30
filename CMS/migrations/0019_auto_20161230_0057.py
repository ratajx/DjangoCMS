# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-29 23:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0018_auto_20161230_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='CMS.News'),
        ),
        migrations.AddField(
            model_name='comment',
            name='site',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='CMS.Site'),
        ),
    ]