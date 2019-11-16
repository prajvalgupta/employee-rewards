# Generated by Django 2.0.7 on 2019-11-15 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('emp_reward', '0008_recievedpoints'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('PAmountReceived', models.IntegerField()),
                ('balanceLeft', models.IntegerField()),
                ('eid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='BalancedPoints',
            new_name='TotalPoints',
        ),
        migrations.RemoveField(
            model_name='recievedpoints',
            name='eid',
        ),
        migrations.DeleteModel(
            name='RecievedPoints',
        ),
    ]