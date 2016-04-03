# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0006_alumni_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='committee',
            name='image',
        ),
        migrations.AlterField(
            model_name='alumni',
            name='image',
            field=models.ImageField(blank=True, help_text='Photo must be round or square! You can can make photo round at cutmypic.com', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='committee_stuff',
            name='image',
            field=models.ImageField(blank=True, help_text='Photo must be round or square! You can can make photo round at cutmypic.com', upload_to='images'),
        ),
    ]
