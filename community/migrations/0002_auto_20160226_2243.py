# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='courses',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='current_company',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='current_occupation',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='time_in_society',
            field=models.CharField(max_length=20),
        ),
    ]
