# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-14 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0029_auto_20180213_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendeeproperty',
            name='manager_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='attendeepropertyvalue',
            name='confirmed',
            field=models.BooleanField(default=True),
        ),
    ]
