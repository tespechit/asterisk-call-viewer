# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-28 14:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asterisk', '0003_auto_20160809_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='cdr',
            name='website',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asterisk.Websites'),
        ),
    ]
