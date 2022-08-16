from django.urls import path

from .views import *

app_name = "feira"

urlpatterns = [
    path("", IndexPageView, name="index"),
]