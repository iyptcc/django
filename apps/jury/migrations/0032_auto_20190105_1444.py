# Generated by Django 2.1.2 on 2019-01-05 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jury', '0031_auto_20181119_1417'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jurorgrade',
            options={'permissions': (('view_results', 'View published results'), ('validate_grades', 'Validate grades after manual check'), ('grade_dump', 'Dump grades and results'), ('member_rank', 'List Ranking of Team Members'))},
        ),
    ]
