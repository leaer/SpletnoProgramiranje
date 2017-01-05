# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 14:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Opravilo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=200)),
                ('createDate', models.DateTimeField(default=datetime.datetime.now)),
                ('dueDate', models.DateTimeField(default=datetime.datetime.now)),
                ('prioriteta', models.CharField(choices=[(1, 'Najmanj pomembno'), (2, 'Pomembno'), (3, 'Zelo pomembno')], default=1, max_length=20)),
                ('podrocje', models.CharField(max_length=20)),
                ('zapiski', models.CharField(max_length=400)),
                ('opravljen', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Uporabnik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=30)),
                ('priimek', models.CharField(max_length=30)),
                ('uporabniskoIme', models.CharField(max_length=20)),
                ('geslo', models.CharField(max_length=30)),
                ('zadnjaPrijava', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='opravilo',
            name='uporabnik',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toDo.Uporabnik'),
        ),
    ]
