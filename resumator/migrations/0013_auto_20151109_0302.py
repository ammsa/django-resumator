# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumator', '0012_auto_20151108_2242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='degree',
        ),
        migrations.AddField(
            model_name='education',
            name='end_date',
            field=models.DateField(null=True, verbose_name='end date', blank=True),
        ),
        migrations.AddField(
            model_name='education',
            name='start_date',
            field=models.DateField(null=True, verbose_name='start date', blank=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='name',
            field=models.CharField(max_length=50, verbose_name='University name'),
        ),
    ]
