# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-15 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0006_auto_20170714_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.FileField(blank=True, default='users/anonim.png', upload_to='comment/', verbose_name='Фото'),
        ),
    ]
