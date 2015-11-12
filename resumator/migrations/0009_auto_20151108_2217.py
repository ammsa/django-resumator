# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumator', '0008_auto_20151108_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='venue',
        ),
        migrations.AddField(
            model_name='publication',
            name='conference',
            field=models.CharField(default=None, max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='authors',
            field=models.CharField(default=None, max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
