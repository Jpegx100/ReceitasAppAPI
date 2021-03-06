# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20170210_1815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='ingredientType',
            new_name='ingredient_type',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='measurementUnit',
            new_name='measurement_unit',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='howToDo',
            new_name='how_to_do',
        ),
        migrations.AlterField(
            model_name='ingredienttype',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
