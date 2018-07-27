# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-06 23:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0012_auto_20161125_1043'),
        ('jury', '0010_juror_conflicting'),
    ]

    operations = [
        migrations.AddField(
            model_name='juror',
            name='availability',
            field=models.ManyToManyField(blank=True, to='plan.Round'),
        ),
        migrations.AddField(
            model_name='juror',
            name='experience',
            field=models.IntegerField(choices=[(0, 'low experience'), (1, 'high experience')], default=0),
        ),
        migrations.AddField(
            model_name='juror',
            name='independent',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='juror',
            name='possible_chair',
            field=models.NullBooleanField(default=False),
        ),
    ]
