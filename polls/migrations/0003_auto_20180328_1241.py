# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-28 12:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0002_options_user_voted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='options',
            name='user_voted',
        ),
        migrations.AddField(
            model_name='question',
            name='user_voted',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
