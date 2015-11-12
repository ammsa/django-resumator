# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumator', '0005_auto_20151108_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicinformation',
            name='github',
            field=models.URLField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basicinformation',
            name='linkedin',
            field=models.URLField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='experience',
            name='URL',
            field=models.URLField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='link',
            field=models.URLField(default='', blank=True),
            preserve_default=False,
        ),
    ]
