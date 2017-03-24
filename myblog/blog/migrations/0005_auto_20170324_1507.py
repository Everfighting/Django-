# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-24 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.CharField(blank=True, choices=[('tech', 'Tech'), ('life', 'Life')], max_length=5, null=True),
        ),
    ]