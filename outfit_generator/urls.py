from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("select_style", views.select_style, name="select-style-page"),
    path("<str:style>", views.outfit_generator, name="outfit-generator-page")
]
