# Generated by Django 2.0.7 on 2019-11-14 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_reward', '0005_auto_20191114_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recievedpoints',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]