# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 00:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Academic', '0001_initial'),
        ('teacher', '0005_attendencemodel_remindermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='remindermodel',
            name='dept_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Academic.Department'),
        ),
    ]
