# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-14 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='device_token',
            new_name='apns_device_token',
        ),
        migrations.AddField(
            model_name='user',
            name='apns_active',
            field=models.BooleanField(default=True),
        ),
    ]
