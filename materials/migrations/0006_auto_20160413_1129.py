# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-13 11:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0005_remove_material_full_discription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='material',
            old_name='short_discription',
            new_name='discription',
        ),
    ]