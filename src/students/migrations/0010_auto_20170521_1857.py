# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_auto_20170521_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]
