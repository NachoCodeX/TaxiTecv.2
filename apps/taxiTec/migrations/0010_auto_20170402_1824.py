# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-02 18:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxiTec', '0009_remove_owner_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='profile',
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
    ]
