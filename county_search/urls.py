from django.urls import path
from . import views

urlpatterns = [
    path("", views.county_search, name="county_search"),
]
