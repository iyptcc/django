# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-11 19:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('printer', '0012_auto_20170311_1346'),
        ('plan', '0022_fight_pdf_partial_grades'),
    ]

    operations = [
        migrations.AddField(
            model_name='fight',
            name='pdf_result',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='result_fight', to='printer.Pdf'),
        ),
    ]
