# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_ml', '0002_auto_20170624_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='desc',
            field=models.CharField(max_length=1000),
        ),
    ]
