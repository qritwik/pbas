# Generated by Django 2.0.2 on 2018-09-21 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facform1', '0030_auto_20180921_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
