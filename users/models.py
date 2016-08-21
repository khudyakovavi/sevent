# coding: utf-8
from datetime import date

from django.contrib.auth.models import AbstractUser
from django.db import models

from sports.models import Sports


class Person(AbstractUser):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=150)
    born = models.DateField()

    sports = models.ManyToManyField(Sports)

    def __unicode__(self):
        return self.name

    @property
    def age(self):
        today = date.today()
        birthday_later = (self.born.month, self.born.day) > (today.month, today.day)
        return today - self.birthday - birthday_later

