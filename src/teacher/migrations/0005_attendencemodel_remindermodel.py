# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 00:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Academic', '0001_initial'),
        ('teacher', '0004_auto_20170521_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendenceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_date', models.DateField(auto_now=True)),
                ('is_attend', models.BooleanField(default=False)),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academic.Course')),
                ('dept_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academic.Department')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.PersonalInformation')),
            ],
            options={
                'ordering': ['-class_date'],
            },
        ),
        migrations.CreateModel(
            name='ReminderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_date', models.DateField(auto_now_add=True)),
                ('course_list', models.CharField(default='', help_text='Example: CSE-101,CSE-102', max_length=250)),
                ('class_time', models.CharField(default='', help_text='Example: CSE-101:10 AM,CSE-102:11 AM', max_length=250)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.PersonalInformation')),
            ],
            options={
                'ordering': ['-class_date'],
            },
        ),
    ]
