# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 13:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voa', '0003_auto_20170207_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='additional',
            name='property',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='voa.Property'),
        ),
    ]
