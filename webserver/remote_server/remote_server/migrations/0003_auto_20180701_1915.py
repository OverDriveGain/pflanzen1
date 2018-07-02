# Generated by Django 2.0.6 on 2018-07-01 19:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('remote_server', '0002_auto_20180618_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='water',
        ),
        migrations.AddField(
            model_name='sensor',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 1, 19, 15, 18, 56664, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pump',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 1, 19, 15, 18, 56977, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pump',
            name='state',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='humidity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='sensor_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='temperature',
            field=models.IntegerField(null=True),
        ),
    ]