# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-16 06:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('when', models.DateTimeField(verbose_name='date of event')),
                ('image', models.ImageField(upload_to='images')),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['when'],
                'db_table': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('attach', models.FileField(upload_to='files')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Materials',
            },
        ),
        migrations.CreateModel(
            name='Workshops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='images')),
            ],
            options={
                'ordering': ['timestamp'],
                'db_table': 'Workshops',
                'verbose_name_plural': 'Workshops',
            },
        ),
    ]
