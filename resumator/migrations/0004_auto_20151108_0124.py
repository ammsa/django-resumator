# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumator', '0003_auto_20151108_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicinformation',
            name='image',
            field=models.ImageField(default='', upload_to=b'', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='picture',
            field=models.ImageField(default='', upload_to=b'', blank=True),
            preserve_default=False,
        ),
    ]
