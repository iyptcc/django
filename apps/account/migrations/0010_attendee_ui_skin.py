# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-24 00:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_participationrole_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='ui_skin',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
