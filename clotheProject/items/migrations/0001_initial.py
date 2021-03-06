# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=125, blank=True)),
                ('price', models.FloatField(default=0, blank=True)),
                ('rating', models.IntegerField(default=0, blank=True)),
                ('description', models.TextField(max_length=300, blank=True)),
                ('photo', models.ImageField(upload_to=b'media/', blank=True)),
                ('barcode', models.CharField(max_length=20, blank=True)),
                ('photo_url', models.URLField(blank=True)),
                ('item_url', models.URLField(blank=True)),
            ],
        ),
    ]
