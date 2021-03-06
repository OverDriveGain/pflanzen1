# Generated by Django 2.0.6 on 2018-06-18 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pump',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(default=0)),
                ('date', models.DateTimeField(verbose_name='date captured')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('node_id', models.IntegerField(primary_key=True, serialize=False)),
                ('water', models.IntegerField(default=0)),
                ('temperature', models.IntegerField(default=0)),
                ('humidity', models.IntegerField(default=0)),
            ],
        ),
    ]
