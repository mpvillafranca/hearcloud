# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-17 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='file_size',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='File size in bytes'),
        ),
    ]
