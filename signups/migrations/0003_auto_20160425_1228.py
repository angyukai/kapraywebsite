# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-25 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0002_remove_designer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designer',
            name='brand',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='designer',
            name='email',
            field=models.EmailField(max_length=500),
        ),
    ]
