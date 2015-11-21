# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'John Smith', max_length=25)),
                ('short_bio', models.CharField(default=b'My short bio', max_length=100, verbose_name='short bio', blank=True)),
                ('long_bio', models.TextField(default=b'My long bio', verbose_name='long bio', blank=True)),
                ('email', models.EmailField(default=b'email@example.com', max_length=254)),
                ('github', models.URLField(null=True)),
                ('linkedin', models.URLField(null=True)),
                ('image', models.ImageField(null=True, upload_to=b'')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('degree', models.CharField(default=None, max_length=10, blank=True)),
                ('abbreviation', models.CharField(default=None, max_length=10, blank=True)),
                ('major', models.CharField(default=None, max_length=15, blank=True)),
                ('gpa', models.CharField(default=None, max_length=10, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=150)),
                ('start_date', models.DateField(verbose_name='start date')),
                ('end_date', models.DateField(verbose_name='end date')),
                ('description', models.TextField(default=None, verbose_name='description')),
                ('URL', models.URLField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('experience', models.ForeignKey(default=None, blank=True, to='resumator.Experience', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(default=None, verbose_name='description', blank=True)),
                ('link', models.URLField()),
                ('picture', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('Authors', models.CharField(default=None, max_length=100, blank=True)),
                ('venue', models.CharField(default=None, max_length=20, blank=True)),
                ('year', models.CharField(default=None, max_length=4, blank=True)),
                ('link', models.URLField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='language',
            name='projects',
            field=models.ForeignKey(default=None, blank=True, to='resumator.Project', null=True),
        ),
    ]
