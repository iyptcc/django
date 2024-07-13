# Generated by Django 2.2.6 on 2019-10-27 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0046_attendeeproperty_edit_multi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendeeproperty',
            name='user_property',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.UserProperty'),
        ),
        migrations.AlterField(
            model_name='attendeepropertyvalue',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.AttendeeProperty'),
        ),
        migrations.AlterField(
            model_name='userpropertyvalue',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.UserProperty'),
        ),
    ]
