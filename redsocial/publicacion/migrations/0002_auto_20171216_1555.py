# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-16 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]