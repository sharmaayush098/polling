# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-26 05:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vote_detail',
            new_name='VoteDetail',
        ),
    ]
