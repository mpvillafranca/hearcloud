# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-21 21:12
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0005_auto_20160818_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='bpm',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(300)], verbose_name='Beats per minute'),
        ),
        migrations.AlterField(
            model_name='song',
            name='release_date',
            field=models.DateField(blank=True, null=True, verbose_name='Complete release date (day-month-year)'),
        ),
        migrations.AlterField(
            model_name='song',
            name='year',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(3000)], verbose_name='Year'),
        ),
    ]
