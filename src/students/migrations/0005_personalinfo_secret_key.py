# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20170521_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='secret_key',
            field=models.CharField(blank=True, max_length=250, null=True, unique=True),
        ),
    ]