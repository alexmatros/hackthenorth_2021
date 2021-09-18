from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("outfit_generator", views.outfit_generator, name="outfit-generator-page")
]
