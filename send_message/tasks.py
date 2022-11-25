from __future__ import absolute_import

import os

from django.conf import settings
from django.core.mail import get_connection
from django.core.mail.message import  EmailMultiAlternatives
from django.template import loader
from celery import shared_task


@shared_task
def send_group(recipients_contexts, subject):
    letters = list()
    for context in recipients_contexts:
        email = EmailMultiAlternatives(
            subject,
            'message',
            settings.EMAIL_HOST_USER,
            (context['email'], )
        )
        email.attach_alternative(
            loader.render_to_string(
                'template.html',
                context
            ),
            'text/html'
        )
        letters.append(email)
    connection = get_connection(fail_silently=False)
    connection.send_messages(letters)
    os.remove('template.html')
