# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-14 10:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_auto_20160226_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumni',
            name='current_company',
        ),
    ]