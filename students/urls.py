from django.urls import path, include
from . import views


urlpatterns = [
    path('student_dash/', views.student_dashboard, name='student_dashboard'),
    path('details/<int:internship_id>/apply/', views.applyPage, name = 'apply'),
    path('mark_as_read/<int:notification_id>', views.mark_as_read, name='mark_as_read'),
    path('applications/', views.MyApplications, name="MyApplications"),
    path('generate_report/', views.generate_report, name = 'generate_report'),
    ]