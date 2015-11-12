# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumator', '0006_auto_20151108_1009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='Authors',
            new_name='authors',
        ),
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateField(null=True, verbose_name='end date', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateField(null=True, verbose_name='start date', blank=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(null=True, verbose_name='end date', blank=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=models.DateField(null=True, verbose_name='start date', blank=True),
        ),
    ]
