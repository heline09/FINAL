from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('application/', views.application, name="application"),
    path('details/', views.details, name="details"),
    path('listings/', views.listings, name='listings'),
    path('students/', views.student_dashboard, name='student_dashboard'), 
    path('recruiters/', views.recruiter_dashboard, name='recruiter_dashboard'),
]
