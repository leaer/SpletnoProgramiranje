# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toDo', '0002_auto_20170104_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opravilo',
            name='prioriteta',
            field=models.CharField(choices=[(1, 'Najmanj pomembno'), (2, 'Pomembno'), (3, 'Zelo pomembno')], default=1, max_length=20),
        ),
    ]