# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 18:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20160929_1818'),
    ]

    operations = [
        migrations.RenameField(
            model_name='example',
            old_name='DOB',
            new_name='name',
        ),
    ]
