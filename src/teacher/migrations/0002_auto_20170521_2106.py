# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinformation',
            name='join_date',
            field=models.CharField(default='', help_text='Format : DD/MM/YYYY,Example : 01/01/1960', max_length=250),
        ),
        migrations.AddField(
            model_name='personalinformation',
            name='mobile_number',
            field=models.CharField(default='', help_text='Format : +8801630603018', max_length=250),
        ),
    ]
