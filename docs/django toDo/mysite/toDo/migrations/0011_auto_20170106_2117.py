# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 20:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toDo', '0010_uporabnik_mail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uporabnik',
            old_name='mail',
            new_name='email',
        ),
    ]