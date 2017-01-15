# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-25 20:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('busside', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_status', models.CharField(max_length=50)),
                ('seat_no', models.CharField(max_length=5)),
                ('seat_type', models.CharField(max_length=20)),
                ('window_seat', models.CharField(max_length=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='buses',
            name='id',
        ),
        migrations.AddField(
            model_name='buses',
            name='available_seats',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='buses',
            name='bus_type',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='buses',
            name='total_seats',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='buses',
            name='bus_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='seats',
            name='bus_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='busside.Buses'),
        ),
    ]
