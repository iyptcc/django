# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-04 11:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0005_room_slug'),
        ('jury', '0002_auto_20161009_1842'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='juror',
            options={'permissions': (('view_juror', 'Can list all jurors and jury plans'),)},
        ),
        migrations.RemoveField(
            model_name='juror',
            name='grades',
        ),
        migrations.RemoveField(
            model_name='jurorgrade',
            name='juror',
        ),
        migrations.AddField(
            model_name='jurorgrade',
            name='juror_session',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='jury.JurorSession'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jurorsession',
            name='grades',
            field=models.ManyToManyField(through='jury.JurorGrade', to='plan.StageAttendance'),
        ),
    ]
