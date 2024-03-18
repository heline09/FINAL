from django.urls import path, include
from . import views


urlpatterns = [
    path('signin/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('skills/', views.skillPage, name="skills"),
    path('logout/',views.logoutUser, name="logout"),
    path('subscribe/', views.subscribePage, name = "subscribePage"),
    path('subscription/user/', views.user_subscriptions, name="user_subscriptions"),
    path('profile/student/<int:user_id>/', views.student_profile, name='student_profile'),
    path('profile/recruiter/<int:user_id>/', views.recruiter_profile, name='recruiter_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    #path('profile/recruiter/<int:user_id>/edit/', views.edit_recruiter_profile, name='edit_recruiter_profile'),

]