# Generated by Django 2.1.8 on 2019-06-02 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0061_auto_20190324_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='publish_juror_availability',
            field=models.BooleanField(default=False),
        ),
    ]
