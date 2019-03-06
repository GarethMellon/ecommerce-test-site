from django.conf.urls import url
from .view import checkout

urlpatterns = [
    url(r'^$', checkout, name = 'checkout'),
    ]