from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('listings/', views.listings, name="listings"),
    path('application/', views.application, name="application"),
    path('signin/', views.loginPage, name="signin"),
    path('register/', views.registerPage, name="register"),
    path('student/', views.student, name="student"),
    path('recruiter/', views.recruiter, name="recruiter"),
    
]
