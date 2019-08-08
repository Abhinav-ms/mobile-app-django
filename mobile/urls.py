from django.conf.urls import url
from django.urls import path

from mobile.views import *

urlpatterns = [
  url(r'^$', index, name='index'),
]