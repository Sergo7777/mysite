# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-15 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0007_auto_20170715_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, default='users/anonim.png', upload_to='comment/', verbose_name='Фото'),
        ),
    ]
