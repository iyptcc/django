# Generated by Django 3.2.1 on 2021-06-19 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0044_auto_20210619_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
