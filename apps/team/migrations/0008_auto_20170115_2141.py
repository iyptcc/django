# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-15 21:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0007_auto_20161213_1247'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'permissions': (('view_teams', 'View all teams'),)},
        ),
    ]
