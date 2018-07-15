# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-13 12:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('num_ID', models.SmallIntegerField()),
                ('operator', models.CharField(choices=[('==', '=='), ('<=', '<='), ('>=', '>='), ('<', '<'), ('>', '>'), ('=!', '=!')], max_length=20)),
                ('second_operand', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=200)),
                ('sended', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('num_ID', models.SmallIntegerField()),
                ('name_ID', models.CharField(max_length=20)),
                ('value', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('unit', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('type', models.CharField(choices=[('BOOL', 'BOOL'), ('INTEGER', 'INTEGER'), ('REAL', 'REAL')], max_length=20)),
                ('widget', models.CharField(choices=[('LIGHT', 'LIGHT'), ('BUTTON', 'BUTTON'), ('SWITCH', 'SWITCH'), ('PARAMETER', 'PARAMETER'), ('DISPLAY', 'DISPLAY')], max_length=20)),
                ('device', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('arguments', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='notification',
            name='first_operand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Tag'),
        ),
        migrations.AddField(
            model_name='notification',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set([('num_ID', 'owner'), ('name_ID', 'owner')]),
        ),
    ]
