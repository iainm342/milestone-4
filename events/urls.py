from . import views
from django.urls import path

urlpatterns = [
    path('', views.post, name='events'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
