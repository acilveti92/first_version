# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-11 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20170104_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='PruebaExcel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.IntegerField(default=0)),
            ],
        ),
    ]
