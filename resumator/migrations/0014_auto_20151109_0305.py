# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumator', '0013_auto_20151109_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='abbreviation',
            field=models.CharField(default=None, max_length=10, verbose_name='Degree abbreviation', blank=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='gpa',
            field=models.CharField(default=None, max_length=10, verbose_name='GPA', blank=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='major',
            field=models.CharField(default=None, max_length=50, blank=True),
        ),
    ]
