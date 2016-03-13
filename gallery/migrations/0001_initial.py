# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 12:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(upload_to='images')),
                ('year', models.CharField(choices=[(2013, '2013'), (2014, '2014'), (2015, '2015'), (2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020')], default=2016, max_length=10)),
                ('title', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Albums',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images')),
                ('title', models.TextField()),
                ('discription', models.TextField()),
                ('album_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Album')),
            ],
            options={
                'db_table': 'Photos',
            },
        ),
    ]
