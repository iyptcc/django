# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-11 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0015_team_is_competing'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='manager',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='teamrole',
            name='type',
            field=models.CharField(blank=True, choices=[('captain', 'Captain'), ('member', 'Member'), ('leader', 'Leader'), ('associated', 'Associated')], max_length=15, null=True),
        ),
    ]
