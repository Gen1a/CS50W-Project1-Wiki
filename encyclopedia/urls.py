from django.urls import path

from . import views

app_name = "wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry_name>", views.show_entry, name="show_entry"),
    path("search/", views.search_entry, name="search_entry"),
    path("create/", views.create_entry, name="create_entry"),
    path("edit/<str:entry_name>", views.edit_entry, name="edit_entry"),
    path("random/", views.random_entry, name="random_entry")
]
