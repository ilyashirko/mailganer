# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Template(models.Model):
    title = models.CharField('Название шаблона', max_length=200)
    
    body = models.TextField('Тело шаблона')

    def __str__(self):
        return self.title.encode('utf-8')


class Message(models.Model):
    subject = models.CharField('Тема письма', max_length=300)
    template = models.ForeignKey(
        'Template',
        verbose_name='Шаблон сообщения',
        related_name='messages',
        on_delete=models.PROTECT
    )
    send_time = models.DateTimeField('Время отправки')
    recipients = models.ManyToManyField(
        'subscribers.Subscriber',
        verbose_name='Получатели',
        related_name='messages',
        help_text='Оставить пустым если надо отправить всем',
        blank=True
    )
    is_sent = models.BooleanField('Отправлено', default=False)

    def __str__(self):
        return self.subject.encode('utf-8')
