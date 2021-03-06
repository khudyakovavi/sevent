# coding: utf-8
from django.db import models


class Sports(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.name
