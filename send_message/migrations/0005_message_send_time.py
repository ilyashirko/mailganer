# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2022-11-25 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_message', '0004_auto_20221124_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='send_time',
            field=models.DateTimeField(default=1999, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438'),
            preserve_default=False,
        ),
    ]
