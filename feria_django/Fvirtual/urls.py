from django.urls import path
from django.urls.resolvers import URLPattern
from.import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('profile/', views.profile, name='profile'),
]