# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-08 02:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxiTec', '0018_car_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingresos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('ingreso', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
