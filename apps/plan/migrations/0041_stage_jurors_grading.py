# Generated by Django 3.1.6 on 2021-03-06 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0040_fight_virtual_server'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='jurors_grading',
            field=models.BooleanField(default=False),
        ),
    ]
