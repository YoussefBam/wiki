from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.generate, name="content_page"),
    path("search/", views.search, name="searched_page")
]
