# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumator', '0015_auto_20151109_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicinformation',
            name='image',
            field=models.ImageField(upload_to=b'media/images', blank=True),
        ),
    ]
