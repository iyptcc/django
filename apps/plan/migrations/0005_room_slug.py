# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-13 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0004_auto_20161009_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
