# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-28 15:18
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0006_site_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
