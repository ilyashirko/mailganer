# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2022-11-23 14:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subscribers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipients', models.ManyToManyField(help_text='\u041e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u043f\u0443\u0441\u0442\u044b\u043c \u0435\u0441\u043b\u0438 \u043d\u0430\u0434\u043e \u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0432\u0441\u0435\u043c', related_name='messages', to='subscribers.Subscriber', verbose_name='\u041f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u0438')),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0448\u0430\u0431\u043b\u043e\u043d\u0430')),
                ('body', models.BooleanField(verbose_name='\u0422\u0435\u043b\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0430')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='messages', to='send_message.Template', verbose_name='\u0428\u0430\u0431\u043b\u043e\u043d \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f'),
        ),
    ]