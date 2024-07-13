# Generated by Django 2.1.5 on 2019-01-19 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_participationrole_attending'),
        ('tournament', '0055_tournament_feedback_permitted_roles'),
    ]

    operations = [
        migrations.AddField(
            model_name='origin',
            name='possible_managers',
            field=models.ManyToManyField(blank=True, to='account.ActiveUser'),
        ),
    ]
