from django.urls import path, include
from . import views

urlpatterns = [
    path('signin/', views.loginPage, name="signin"),
    path('register/', views.registerPage, name="register"),
    path('student/', views.student, name="student"),
    path('recruiter/', views.recruiter, name="recruiter"),
    

]