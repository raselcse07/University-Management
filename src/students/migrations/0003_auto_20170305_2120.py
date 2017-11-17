# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_personalinfo_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='email',
            field=models.EmailField(default='', max_length=255, unique=True, verbose_name='email address'),
        ),
    ]