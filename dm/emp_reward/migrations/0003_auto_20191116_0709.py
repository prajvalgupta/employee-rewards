# Generated by Django 2.0.7 on 2019-11-16 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_reward', '0002_auto_20191116_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointtrans',
            name='PTransDate',
            field=models.DateTimeField(null=True),
        ),
    ]
