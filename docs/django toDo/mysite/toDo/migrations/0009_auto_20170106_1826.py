# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toDo', '0008_auto_20170106_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opravilo',
            name='podrocje',
            field=models.CharField(choices=[('1', 'Šola'), ('2', 'Delo'), ('3', 'Dom'), ('4', 'Nakupovanje'), ('5', 'Ostalo')], default=1, max_length=1),
        ),
    ]
