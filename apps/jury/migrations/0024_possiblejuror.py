# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-26 08:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_auto_20180225_1101'),
        ('tournament', '0044_auto_20180219_1437'),
        ('jury', '0023_auto_20180115_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='PossibleJuror',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.IntegerField(choices=[(-1, 'no experience'), (0, 'low experience'), (1, 'high experience')], default=0)),
                ('approved_at', models.DateTimeField(auto_now_add=True)),
                ('approved_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='approved_possiblejurors', to='account.ActiveUser')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.ActiveUser')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Tournament')),
            ],
        ),
    ]
