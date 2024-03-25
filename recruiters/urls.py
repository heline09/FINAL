from django.urls import path, include
from . import views

urlpatterns = [
    path('recruiter_dash/', views.recruiter_dashboard, name='recruiter_dashboard'),
    path('applicants/<int:internship_id>/', views.applicant_list, name='applicant_list'),
    path('applicant_details/<int:application_id>/', views.applicant_details, name="applicant_details"),
    path('download_cv/<int:application_id>/', views.download_cv, name='download_cv'),
    path('generate_pdf_report/', views.generate_pdf_report, name = 'generate_pdf_report'),
    path('posts/', views.posts, name="posts"),
    path('posted/', views.posted, name="posted"),
    path('posted/<int:id>/', views.update_internship, name="update_internship"),
    path('deactivate_internship/<int:internship_id>/', views.deactivate_internship, name='deactivate_internship'),
    path('confirmation_status_check/<int:application_id>/', views.confirmation_status_check, name='confirmation_status_check'),
]