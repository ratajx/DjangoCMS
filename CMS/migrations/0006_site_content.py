# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-28 15:15
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0005_remove_site_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='content',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]