# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-19 09:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facform1', '0026_auto_20180919_0941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ipr_status',
            old_name='ipr',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='ipr_type',
            old_name='ipr',
            new_name='name',
        ),
    ]
