# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-12 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0016_auto_20180211_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='notify_applications',
            field=models.BooleanField(default=True, verbose_name='Notify Managers by Email for new Applications'),
        ),
    ]
