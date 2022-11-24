# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Subscriber

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'birthday', 'email')
    readonly_fields = ('joined_at',)