# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 17:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toDo', '0005_auto_20170105_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uporabnik',
            name='zadnjaPrijava',
        ),
    ]
