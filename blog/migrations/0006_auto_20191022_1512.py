# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-10-22 07:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20191022_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='desc',
            field=models.CharField(max_length=255, verbose_name='简介'),
        ),
    ]