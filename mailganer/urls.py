from __future__ import absolute_import

from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^letters/', include('send_message.urls')),
]
