# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Message, Template
from subscribers.models import Subscriber
from tasks import send_group


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    
    def send_message(self, request, queryset):
        for message in queryset.prefetch_related('template', 'recipients'):
            with open('template.html', 'w') as template_file:
                    template_file.write(message.template.body.encode('utf-8'))
            recipients = message.recipients.all() or Subscriber.objects.all()
            recipients_contexts = list()
            for recipient in recipients:
                recipients_contexts.append(
                    {
                        'firstname': recipient.firstname,
                        'lastname': recipient.lastname,
                        'birthday': recipient.birthday,
                        'email': recipient.email
                    }
                )
            send_group.apply_async(args=[recipients_contexts, message.subject])
            message.is_sent = True
            message.save()

    send_message.short_description = "Send message(-s)"

    list_display = ('subject', 'is_sent')
    actions = [send_message]
    filter_horizontal = ('recipients', )