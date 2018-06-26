# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-20 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20180613_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='widget',
            field=models.CharField(choices=[('LIGHT', 'LIGHT'), ('BUTTON', 'BUTTON'), ('SWITCH', 'SWITCH'), ('PARAMETER', 'PARAMETER'), ('DISPLAY', 'DISPLAY')], max_length=20),
        ),
    ]