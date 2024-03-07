from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('details/<int:internship_id>/', views.details, name="details"),
    path('listings/', views.listings, name='listings'),
]
