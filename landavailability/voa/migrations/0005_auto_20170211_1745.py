# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 17:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voa', '0004_additional_property'),
    ]

    operations = [
        migrations.RenameField(
            model_name='additional',
            old_name='property',
            new_name='additional_property',
        ),
        migrations.RenameField(
            model_name='adjustment',
            old_name='property',
            new_name='adjustment_property',
        ),
        migrations.RenameField(
            model_name='area',
            old_name='property',
            new_name='area_property',
        ),
    ]
