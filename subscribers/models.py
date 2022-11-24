# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Subscriber(models.Model):
    firstname = models.CharField('Имя', max_length=50)
    lastname = models.CharField('Фамилия', max_length=50)
    patronymic = models.CharField('Отчество', max_length=50, blank=True)

    birthday = models.DateField('Дата рождения')

    email = models.EmailField('E-mail')

    joined_at = models.DateTimeField('Добавлен', auto_now_add=True)

    def __str__(self):
        return '{} {} ({})'.encode('utf-8').format(
            self.firstname.encode('utf-8'),
            self.lastname.encode('utf-8'),
            self.email.encode('utf-8')
        )
