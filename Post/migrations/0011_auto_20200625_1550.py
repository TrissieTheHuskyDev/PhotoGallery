# Generated by Django 2.2.12 on 2020-06-25 10:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0010_auto_20200625_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 25, 10, 20, 57, 891119, tzinfo=utc)),
        ),
    ]