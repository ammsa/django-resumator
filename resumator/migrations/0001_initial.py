# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import colorful.fields


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
                ('github', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
                ('image', models.ImageField(upload_to=b'images', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='University name')),
                ('abbreviation', models.CharField(default=None, max_length=10, verbose_name='Degree abbreviation', blank=True)),
                ('start_date', models.DateField(null=True, verbose_name='start date', blank=True)),
                ('end_date', models.DateField(null=True, verbose_name='end date', blank=True)),
                ('major', models.CharField(default=None, max_length=50, blank=True)),
                ('gpa', models.CharField(default=None, max_length=10, verbose_name='GPA', blank=True)),
            ],
            options={
                'ordering': ['-end_date'],
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=150)),
                ('start_date', models.DateField(null=True, verbose_name='start date', blank=True)),
                ('end_date', models.DateField(null=True, verbose_name='end date', blank=True)),
                ('description', models.TextField(default=None, verbose_name='description')),
                ('link', models.URLField(blank=True)),
                ('image', models.ImageField(upload_to=b'images', blank=True)),
            ],
            options={
                'ordering': ['-end_date'],
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('experience', models.ManyToManyField(to='resumator.Experience', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(default=None, verbose_name='description', blank=True)),
                ('start_date', models.DateField(null=True, verbose_name='start date', blank=True)),
                ('end_date', models.DateField(null=True, verbose_name='end date', blank=True)),
                ('link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('authors', models.CharField(max_length=200, blank=True)),
                ('conference', models.CharField(max_length=200, blank=True)),
                ('abstract', models.TextField(blank=True)),
                ('year', models.CharField(max_length=4, blank=True)),
                ('link', models.URLField(blank=True)),
            ],
            options={
                'ordering': ['-year'],
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('base_color', colorful.fields.RGBColorField(default=b'bc0000', verbose_name='Base color')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('abbreviation', models.CharField(unique=True, max_length=5, verbose_name='Tag abbreviation')),
            ],
        ),
        migrations.AddField(
            model_name='publication',
            name='tags',
            field=models.ManyToManyField(related_name='publications', to='resumator.Tag', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(related_name='projects', to='resumator.Tag', blank=True),
        ),
        migrations.AddField(
            model_name='language',
            name='projects',
            field=models.ManyToManyField(to='resumator.Project', blank=True),
        ),
    ]
