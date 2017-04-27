# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 21:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Whstock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dsc', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amazon.Whstock'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
