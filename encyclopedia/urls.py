from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.generate, name="content_page"),
    path("search/", views.search, name="searched_page"),
    #rendering add.html
    path("create/", views.view_create, name="view_create"),
    #path to add desired page to database
    path("create_page/", views.create , name="created_page"),
    #path to get what page user wants to edit
    path("edit/<str:title>",views.edit, name="edit_page"),
    #path of edit version
    path("edited/<str:title>",views.save, name="edit_page"),
    path("random/",views.random, name="random")
]
