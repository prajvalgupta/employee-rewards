# Generated by Django 2.0.7 on 2019-11-15 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp_reward', '0006_auto_20191114_2251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recievedpoints',
            name='eid',
        ),
        migrations.DeleteModel(
            name='RecievedPoints',
        ),
    ]