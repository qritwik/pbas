# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-17 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facform1', '0016_auto_20180916_1954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedbacktab',
            old_name='e_t4_stu_perpass',
            new_name='e_l4_stu_perpass',
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='last name'),
        ),
    ]
