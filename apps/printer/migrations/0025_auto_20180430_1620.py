# Generated by Django 2.0.3 on 2018-04-30 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0011_account_address'),
        ('printer', '0024_template_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdf',
            name='invoice_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bank.Account'),
        ),
        migrations.AlterField(
            model_name='defaulttemplate',
            name='type',
            field=models.CharField(choices=[('preview', 'Preview'), ('ranking', 'Ranking'), ('results', 'Results'), ('jury_round', 'Jury Round Plan'), ('team_round', 'Team Round Plan'), ('jury_feedback', 'Jury Fight Feedback'), ('problem_select', 'Problem Selection for last PF'), ('persons', 'Persons'), ('registration', 'Registration'), ('invoice', 'Invoice')], max_length=25),
        ),
        migrations.AlterField(
            model_name='pdftag',
            name='type',
            field=models.CharField(blank=True, choices=[('preview', 'Preview'), ('ranking', 'Ranking'), ('results', 'Results'), ('jury_round', 'Jury Round Plan'), ('team_round', 'Team Round Plan'), ('jury_feedback', 'Jury Fight Feedback'), ('problem_select', 'Problem Selection for last PF'), ('persons', 'Persons'), ('registration', 'Registration'), ('invoice', 'Invoice')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='template',
            name='type',
            field=models.CharField(blank=True, choices=[('preview', 'Preview'), ('ranking', 'Ranking'), ('results', 'Results'), ('jury_round', 'Jury Round Plan'), ('team_round', 'Team Round Plan'), ('jury_feedback', 'Jury Fight Feedback'), ('problem_select', 'Problem Selection for last PF'), ('persons', 'Persons'), ('registration', 'Registration'), ('invoice', 'Invoice')], max_length=25, null=True),
        ),
    ]
