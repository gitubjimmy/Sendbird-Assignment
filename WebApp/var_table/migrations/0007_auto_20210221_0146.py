# Generated by Django 2.2.18 on 2021-02-20 16:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('var_table', '0006_auto_20210221_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variables',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 20, 16, 46, 14, 198454, tzinfo=utc)),
        ),
    ]