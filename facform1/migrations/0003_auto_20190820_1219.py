# Generated by Django 2.0.2 on 2019-08-20 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facform1', '0002_auto_20190817_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pic/'),
        ),
    ]
