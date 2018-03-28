# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-28 10:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='options',
            name='user_voted',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]