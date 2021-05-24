from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostList.as_view(), name="events"),
    path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
]
