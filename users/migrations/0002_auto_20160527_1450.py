# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-27 12:50
from __future__ import unicode_literals

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='profile_images'),
        ),
    ]
