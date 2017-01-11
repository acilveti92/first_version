# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-30 20:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_wordsuse_autotrans'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordAjax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wordRef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Word')),
            ],
        ),
    ]