# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0005_transaction_package_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='product_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='transaction',
            name='product_num',
            field=models.IntegerField(default=-1),
        ),
    ]
