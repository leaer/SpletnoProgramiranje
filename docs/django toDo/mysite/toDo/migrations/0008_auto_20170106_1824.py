# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toDo', '0007_auto_20170106_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opravilo',
            name='prioriteta',
            field=models.CharField(choices=[('1', 'Najmanj pomembno'), ('2', 'Pomembno'), ('3', 'Zelo pomembno')], default=1, max_length=1),
        ),
    ]
