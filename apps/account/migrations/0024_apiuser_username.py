# Generated by Django 2.1.5 on 2019-03-17 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0023_auto_20190316_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='apiuser',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
