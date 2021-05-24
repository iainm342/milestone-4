from . import views
from django.urls import path

urlpatterns = [
    path('', views.post, name='post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
