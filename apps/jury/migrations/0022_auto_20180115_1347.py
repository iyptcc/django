# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-15 13:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_participationrole_groups'),
        ('jury', '0021_auto_20170705_0407'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignresult',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Attendee'),
        ),
        migrations.AddField(
            model_name='assignresult',
            name='cooling_base',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assignresult',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='assignresult',
            name='finished',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assignresult',
            name='room_jurors',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assignresult',
            name='total_rounds',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
