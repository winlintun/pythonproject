from django.urls import path
from . import views

#create new urls file


urlpatterns = [
path("<int:id>", views.index, name='index'),
path("", views.home, name='home'),


]