# Generated by Django 2.1.5 on 2019-03-16 16:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fight', '0002_auto_20190316_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clockstate',
            name='server_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
