# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumator', '0009_auto_20151108_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='abstract',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='authors',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='conference',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='year',
            field=models.CharField(max_length=4, blank=True),
        ),
    ]
