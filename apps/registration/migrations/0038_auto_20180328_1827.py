# Generated by Django 2.0.3 on 2018-03-28 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0037_auto_20180328_1827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendeepropertyvalue',
            old_name='att_property',
            new_name='property',
        ),
    ]
