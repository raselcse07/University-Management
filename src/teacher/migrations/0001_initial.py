# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 20:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import teacher.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Academic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(default='', max_length=255, unique=True, verbose_name='email address')),
                ('educational_background', models.TextField()),
                ('fathers_name', models.CharField(max_length=250)),
                ('mothers_name', models.CharField(max_length=250)),
                ('birthday', models.CharField(help_text='Format : DD/MM/YYYY,Example : 01/01/1960', max_length=250)),
                ('blood_group', models.CharField(help_text='Example : AB+', max_length=20)),
                ('TrxID', models.CharField(blank=True, max_length=250, null=True, unique=True, verbose_name='Password')),
                ('height_field', models.IntegerField(default=100)),
                ('width_field', models.IntegerField(default=100)),
                ('teacher_image', models.ImageField(default='', height_field='height_field', upload_to=teacher.models.upoload_location, width_field='width_field')),
                ('dept_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academic.Department')),
            ],
            options={
                'verbose_name': 'Personal Information',
                'verbose_name_plural': 'Personal Infomations',
                'ordering': ['name'],
            },
        ),
    ]
