# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-03-28 04:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200328_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]
