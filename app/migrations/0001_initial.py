# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-12 14:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='photos size must be 1280\u2006\xd7\u2006720 ', upload_to='images')),
            ],
            options={
                'db_table': 'Slider',
                'verbose_name': 'photo',
                'verbose_name_plural': 'Slides',
            },
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='images')),
                ('link', models.URLField(help_text='sponsors link, url like : http://google.com')),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'Sponsors',
            },
        ),
        migrations.CreateModel(
            name='Visits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Visit',
                'verbose_name': 'Visit',
                'verbose_name_plural': 'Visits',
            },
        ),
    ]