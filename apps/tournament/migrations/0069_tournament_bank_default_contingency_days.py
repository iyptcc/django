# Generated by Django 2.2.9 on 2020-03-07 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0068_tournament_allow_oauth'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='bank_default_contingency_days',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
