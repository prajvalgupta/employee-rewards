# Generated by Django 2.0.7 on 2019-11-14 22:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('emp_reward', '0004_auto_20191114_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recievedpoints',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 14, 22, 49, 26, 624475, tzinfo=utc)),
        ),
    ]
