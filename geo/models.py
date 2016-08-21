# coding: utf-8
from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)

    location = models.CharField(max_length=150)
    address = models.CharField(max_length=150, null=True, blank=True)

    def __unicode__(self):
        return self.name
