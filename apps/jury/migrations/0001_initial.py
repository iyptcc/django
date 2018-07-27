# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-09 16:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tournament', '0002_auto_20161009_0118'),
        ('account', '0003_auto_20161009_0022'),
        ('plan', '0004_auto_20161009_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Juror',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='JurorGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.FloatField()),
                ('valid', models.BooleanField(default=False)),
                ('juror', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jury.Juror')),
                ('stage_attendee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.StageAttendance')),
            ],
        ),
        migrations.CreateModel(
            name='JurorRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Tournament')),
            ],
        ),
        migrations.CreateModel(
            name='JurorSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.Fight')),
                ('juror', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jury.Juror')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jury.JurorRole')),
            ],
        ),
        migrations.AddField(
            model_name='juror',
            name='fights',
            field=models.ManyToManyField(through='jury.JurorSession', to='plan.Fight'),
        ),
        migrations.AddField(
            model_name='juror',
            name='grades',
            field=models.ManyToManyField(through='jury.JurorGrade', to='plan.StageAttendance'),
        ),
        migrations.AddField(
            model_name='juror',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.Attendee'),
        ),
    ]
