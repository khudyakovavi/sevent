# coding: utf-8
from django.contrib.auth.models import AbstractUser
from django.db import models


class Person(AbstractUser):
    city = models.CharField(max_length=150)
    age = models.PositiveSmallIntegerField()
