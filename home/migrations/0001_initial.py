# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-04 21:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.TextField(max_length=200)),
                ('images', models.TextField(max_length=500)),
                ('video', models.TextField(max_length=200)),
                ('words', models.TextField(max_length=1000)),
                ('filepath', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]