from django.conf.urls import url
from .views import *

app_name = 'eddies'
urlpatterns = [
    url(r'^$', eddies, name="eddies"),
]