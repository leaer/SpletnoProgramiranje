# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 16:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toDo', '0016_auto_20170108_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opravilo',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='opravilo',
            name='dueDate',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
