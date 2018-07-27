# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-01 13:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20170909_2138'),
        ('registration', '0009_auto_20171125_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertyvalue',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='account.ActiveUser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='propertyvalue',
            name='creation',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
