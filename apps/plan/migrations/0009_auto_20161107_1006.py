# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-07 10:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0008_auto_20161105_1957'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fight',
            options={'permissions': (('view_fight_operator', 'Can list fight operators/locks'), ('change_fight_operator', 'Can change fight operators/locks'))},
        ),
    ]
