# Generated by Django 2.2.18 on 2021-02-20 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('var_table', '0004_variables_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variables',
            name='type',
        ),
    ]
