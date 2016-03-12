from __future__ import unicode_literals

from django.db import models


class Committee(models.Model):
    class Meta():
        db_table = "Committee"

    def __str__(self):
        return self.time

    time = models.TextField('years')
    image = models.ImageField(upload_to='images')

    def get_absolute_url(self):
        return "/committee/%i/" % self.time


class Committee_stuff(models.Model):
    class Meta():
        db_table = "Stuff"
        verbose_name = "member"
        verbose_name_plural = "Current stuff"

    def __str__(self):
        return self.name

    name = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    discription = models.TextField()
    image = models.ImageField(upload_to='images')
    committee = models.ForeignKey(Committee)


class Alumni(models.Model):
    class Meta():
        db_table = "Alumni"
        verbose_name_plural = 'Alumnies'

    def __str__(self):
        return self.last_name + ' ' + self.first_name

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    facebook = models.URLField()
    linkedin = models.URLField()
    time_in_society = models.CharField(max_length=20)
    courses = models.CharField(max_length=200)
    current_occupation = models.CharField(max_length=200)
    current_company = models.CharField(max_length=200)
