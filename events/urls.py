from . import views
from django.urls import path

urlpatterns = [
    path("", views.post, name="events"),
    path("detail<slug:slug>/", views.post_detail, name="post_detail"),
    path("add_event/", views.add_post, name="add_post"),
]
