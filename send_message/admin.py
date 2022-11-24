# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import smtplib

from email.mime.text import MIMEText
from django.contrib import admin
from django.template import Template as django_template_object, Context

from mailganer import settings
from models import Message, Template
from subscribers.models import Subscriber


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    
    def send_message(self, request, queryset):
        connection = smtplib.SMTP_SSL(settings.EMAIL_HOST)
        connection.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        

        for message in queryset.prefetch_related('template', 'recipients'):
            subject = message.subject
            template = django_template_object(message.template.body)
            recipients = message.recipients.all() or Subscriber.objects.all()

            for recipient in recipients:
                context = {
                    'firstname': recipient.firstname,
                    'lastname': recipient.lastname,
                    'birthday': recipient.birthday,
                    'email': recipient.email
                }
                letter = MIMEText(template.render(Context(context)).encode('utf-8'), 'html', 'utf-8')
                letter['Subject'] = subject
                letter['From'] = settings.EMAIL_HOST_USER
                letter['To'] = context['email']
                connection.sendmail(
                    settings.EMAIL_HOST_USER,
                    [context['email'], ],
                    letter.as_string()
                )
            message.is_sent = True
            message.save()
        
        connection.quit()

    send_message.short_description = "Send message(-s)"

    list_display = ('subject', 'is_sent')
    actions = [send_message]
    filter_horizontal = ('recipients', )