# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-14 18:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_participationrole_attending'),
        ('team', '0017_auto_20180212_0733'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='teammember',
            unique_together=set([('attendee', 'team')]),
        ),
    ]
