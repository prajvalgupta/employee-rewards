# Generated by Django 2.0.7 on 2019-11-15 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_reward', '0012_auto_20191115_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointtrans',
            name='PTransDate',
            field=models.DateField(null=True),
        ),
    ]
