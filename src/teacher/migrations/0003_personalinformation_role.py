# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20170521_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinformation',
            name='role',
            field=models.CharField(default='', max_length=250),
        ),
    ]
