# Generated by Django 2.0.7 on 2019-11-14 22:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('emp_reward', '0003_auto_20191114_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recievedpoints',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 14, 22, 48, 42, 6012, tzinfo=utc)),
        ),
    ]
