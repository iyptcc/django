# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-13 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0009_auto_20161212_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='origin',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
