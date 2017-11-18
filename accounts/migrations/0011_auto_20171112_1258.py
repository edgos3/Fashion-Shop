# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20171112_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='house_number_name',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='address',
            name='postcode',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='address',
            name='town',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
