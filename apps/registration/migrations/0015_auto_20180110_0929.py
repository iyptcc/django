# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-10 09:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0014_auto_20180109_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('int', 'Integer'), ('string', 'String'), ('datetime', 'datetime'), ('date', 'date'), ('image', 'image'), ('text', 'text'), ('gender', 'gender'), ('preferred_name', 'preferred name'), ('preferred_name_short', 'preferred name short'), ('choice', 'Select One'), ('multiple_choice', 'Select Multiple')], max_length=30)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='attendeeproperty',
            options={'ordering': ('order',)},
        ),
        migrations.RemoveField(
            model_name='attendeeproperty',
            name='id',
        ),
        migrations.RemoveField(
            model_name='attendeeproperty',
            name='name',
        ),
        migrations.RemoveField(
            model_name='attendeeproperty',
            name='type',
        ),
        migrations.RemoveField(
            model_name='userproperty',
            name='id',
        ),
        migrations.RemoveField(
            model_name='userproperty',
            name='name',
        ),
        migrations.RemoveField(
            model_name='userproperty',
            name='order',
        ),
        migrations.RemoveField(
            model_name='userproperty',
            name='type',
        ),
        migrations.AddField(
            model_name='attendeeproperty',
            name='property_ptr',
            field=models.OneToOneField(auto_created=True, default='', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='registration.Property'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userproperty',
            name='property_ptr',
            field=models.OneToOneField(auto_created=True, default='', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='registration.Property'),
            preserve_default=False,
        ),
    ]
