# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-24 06:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170316_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]