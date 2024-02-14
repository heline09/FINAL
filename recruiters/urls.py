from django.urls import path, include
from . import views

urlpatterns = [
    path('recruiter_dash/', views.recruiter_dashboard, name='recruiter_dashboard'),
    path('posts/', views.posts, name="posts"),
    path('posted/', views.posted, name="posted"),
]