# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-03-26 05:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_type', models.CharField(max_length=15)),
                ('total_number', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.CharField(max_length=1000),
        ),
    ]
