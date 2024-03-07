from django.urls import path, include
from . import views


urlpatterns = [
    path('student_dash/', views.student_dashboard, name='student_dashboard'),
    path('details/<int:internship_id>/apply/', views.applyPage, name = 'apply'),
    path('applications/', views.MyApplications, name="MyApplications"),

]