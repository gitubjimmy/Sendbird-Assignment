# Generated by Django 2.2.18 on 2021-02-20 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('var_table', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variables',
            old_name='Value',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='Variable_name',
            new_name='value',
        ),
    ]
