# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-26 09:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jury', '0024_possiblejuror'),
    ]

    operations = [
        migrations.AlterField(
            model_name='possiblejuror',
            name='approved_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='possiblejuror',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approved_possiblejurors', to='account.ActiveUser'),
        ),
    ]
