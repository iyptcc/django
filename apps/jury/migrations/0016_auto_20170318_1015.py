# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-18 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jury', '0015_auto_20170115_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juror',
            name='experience',
            field=models.IntegerField(choices=[(-1, 'no experience'), (0, 'low experience'), (1, 'high experience')], default=0),
        ),
    ]
