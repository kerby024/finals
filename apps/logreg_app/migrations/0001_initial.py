# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 21:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('alias', models.CharField(max_length=255)),
                ('email_address', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('dob', models.DateField()),
            ],
        ),
    ]
