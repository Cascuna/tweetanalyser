# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 00:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sentiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('minimum_sentiment', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=30)),
                ('sentiment_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('actual_tweet', models.CharField(max_length=300)),
                ('date_time', models.DateTimeField()),
            ],
        ),
    ]
