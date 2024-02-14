from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('application/', views.application, name="application"),
    path('details/<int:internship_id>/', views.details, name="details"),
    path('listings/', views.listings, name='listings'),
]
