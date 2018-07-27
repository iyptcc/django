# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-11 09:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('printer', '0011_auto_20170309_1001'),
        ('plan', '0021_fight_pdf_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='fight',
            name='pdf_partial_grades',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fight_partial', to='printer.Pdf'),
        ),
    ]
