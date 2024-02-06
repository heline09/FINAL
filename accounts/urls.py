from django.urls import path, include
from . import views

urlpatterns = [
    path('signin/', views.loginPage, name="signin"),
    path('register/', views.registerPage, name="register"),
    path('recruiter/', views.recruiter, name="recruiter"),
    path('logout/',views.logoutUser, name="logout"),
    

]