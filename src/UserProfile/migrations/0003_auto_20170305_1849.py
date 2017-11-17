# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 18:49
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(max_length=250, unique=True, validators=[django.core.validators.RegexValidator(code='invalid username', message='Username must be Alphanumeric and contain any of the following : ". @ + - _ "', regex='^[a-zA-Z0-9.@+-_]*$')]),
        ),
    ]
