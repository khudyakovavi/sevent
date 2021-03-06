# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-21 10:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sports', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('geo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SportEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('date', models.DateTimeField()),
                ('start_age', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('end_age', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('A', 'All'), ('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_events', to=settings.AUTH_USER_MODEL)),
                ('participants', models.ManyToManyField(related_name='events', to=settings.AUTH_USER_MODEL)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo.Place')),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sports.Sports')),
            ],
        ),
    ]
