# Generated by Django 3.1.4 on 2020-12-08 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_transacao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transacao',
            options={'verbose_name_plural': 'Transações'},
        ),
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='observacoes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
