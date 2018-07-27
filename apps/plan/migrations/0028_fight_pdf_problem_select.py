# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-07 12:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('printer', '0019_auto_20170707_1250'),
        ('plan', '0027_fight_pdf_jury_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='fight',
            name='pdf_problem_select',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='problem_select', to='printer.Pdf'),
        ),
    ]
