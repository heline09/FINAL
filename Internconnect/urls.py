from django.urls import path, include
from . import views
from .views import internship_list

urlpatterns = [
    path('', views.home, name="home"),
    path('listings/', views.listings, name="listings"),
    path('application/', views.application, name="application"),
    path('details/', views.details, name="details"),
    path('api/internships/', views.internship_list, name='internship_list'),
]
