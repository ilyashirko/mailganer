
from __future__ import absolute_import

from datetime import datetime
# from urllib import urljoin

import pytz
        
from django.contrib import admin

from .models import Message, Template
from subscribers.models import Subscriber
from .tasks import send_group
from django.urls import reverse, reverse_lazy


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    def get_eta(self, schedule):
        utc = pytz.UTC
        if datetime.now().replace(tzinfo=utc) < schedule.replace(tzinfo=utc):
            return schedule

    def get_reading_confirmation_pixel_url(self, request, subscriber_id, message_id):
        confirmation_path = reverse_lazy('letter_opened').encode('utf-8') + \
            '{}/{}'.format(subscriber_id, message_id)
        return request.build_absolute_uri(confirmation_path)


    def send_message(self, request, queryset):
        for message in queryset.prefetch_related('template', 'recipients'):
            with open('template.html', 'w') as template_file:
                    template_file.write(message.template.body.encode('utf-8'))
            recipients = message.recipients.all() or Subscriber.objects.all()
            recipients_contexts = list()
            for recipient in recipients:
                open_pixel_url = self.get_reading_confirmation_pixel_url(request, recipient.id, message.id)
                recipients_contexts.append(
                    {
                        'firstname': recipient.firstname,
                        'lastname': recipient.lastname,
                        'birthday': recipient.birthday,
                        'email': recipient.email,
                        'open_pixel_url': open_pixel_url
                    }
                )
            send_group.apply_async(
                args=[recipients_contexts, message.subject],
                eta=self.get_eta(message.send_time)
            )
            message.is_sent = True
            message.save()

    send_message.short_description = "Send message(-s)"

    list_display = ('subject', 'is_sent')
    actions = [send_message]
    filter_horizontal = ('recipients', )