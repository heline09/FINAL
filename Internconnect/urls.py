from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('listings/', views.listings, name="listings"),
    path('application/', views.application, name="application"),
    path('description/', views.description, name="description"),
    
]
