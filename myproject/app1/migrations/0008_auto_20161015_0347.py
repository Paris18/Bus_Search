# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-15 03:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20160929_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
