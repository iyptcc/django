# Generated by Django 2.1.9 on 2019-07-09 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0036_round_publish_jurors'),
    ]

    operations = [
        migrations.AddField(
            model_name='fight',
            name='publish_partials',
            field=models.BooleanField(default=False),
        ),
    ]
