from . import views
from django.urls import path

urlpatterns = [
    path("", views.post, name="events"),
    path("detail/<slug:slug>/", views.post_detail, name="post_detail"),
    path("add_event/", views.add_post, name="add_post"),
    path("edit_event/<slug:slug>/", views.edit_post, name="edit_post"),
    path("delete_event/<slug:slug>/", views.delete_post, name="delete_post"),
]
