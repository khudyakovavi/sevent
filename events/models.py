# coding: utf-8
from django.db import models

from geo.models import Place
from sports.models import Sports
from users.models import Person

from .constants import GENDER_CHOICES


class SportEvent(models.Model):
    title = models.CharField(max_length=256)
    date = models.DateTimeField()

    sport = models.ForeignKey(Sports)
    place = models.ForeignKey(Place)
    owner = models.ForeignKey(Person, related_name='owned_events')
    participants = models.ManyToManyField(Person, related_name='events')

    start_age = models.PositiveSmallIntegerField(null=True, blank=True)
    end_age = models.PositiveSmallIntegerField(null=True, blank=True)

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __unicode__(self):
        return self.title
