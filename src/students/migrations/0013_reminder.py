# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 20:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Academic', '0001_initial'),
        ('students', '0012_term_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_date', models.DateField(auto_now_add=True)),
                ('course_list', models.CharField(default='', help_text='Example: CSE-101,CSE-102', max_length=250)),
                ('exam_time', models.CharField(default='', help_text='Example: CSE-10 AM,CSE-11 AM', max_length=250)),
                ('dept_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academic.Department')),
                ('reg_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.PersonalInfo')),
            ],
            options={
                'ordering': ['-exam_date'],
            },
        ),
    ]