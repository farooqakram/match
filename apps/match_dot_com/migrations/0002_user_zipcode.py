# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match_dot_com', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='zipcode',
            field=models.IntegerField(default=60513),
            preserve_default=False,
        ),
    ]
