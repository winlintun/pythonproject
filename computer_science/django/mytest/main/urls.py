from django.contrib import admin
from django.db.models.fields import URLField
from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name='index')
]
