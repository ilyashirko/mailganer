from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^opened/<int:subscriber_id>/<int:message_id>', views.letter_opened, name='letter_opened'),
]
