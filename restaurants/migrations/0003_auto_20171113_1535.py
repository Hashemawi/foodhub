# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 15:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20171106_1651'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurant',
            options={'ordering': ['-name']},
        ),
    ]