# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-01 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_auto_20170324_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordsuse',
            name='aparitions_hk',
            field=models.IntegerField(default=0),
        ),
    ]
