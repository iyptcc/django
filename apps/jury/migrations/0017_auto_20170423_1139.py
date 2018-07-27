# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-23 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0023_fight_pdf_result'),
        ('jury', '0016_auto_20170318_1015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jurorsession',
            options={'ordering': ['order'], 'permissions': (('change_all_jurorsessions', 'Can change jury any time'), ('assign_jurors', 'Can assign jurors to fights'), ('delete_all_jurorsessions', 'Delete all juror sessions together'))},
        ),
        migrations.AddField(
            model_name='jurorsession',
            name='order',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='jurorsession',
            unique_together=set([('order', 'fight')]),
        ),
    ]
