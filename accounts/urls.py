from django.urls import path, include
from . import views


urlpatterns = [
    path('signin/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('skills/', views.skillPage, name="skills"),
    path('logout/',views.logoutUser, name="logout"),
    path('subscription/plans/', views.subscription_plans, name="subscription_plans"),
    path('subscription/choose/<int:plan_id>/', views.choose_subscription, name="choose_subscription"),
    path('subscription/user/', views.user_subscriptions, name="user_subscriptions"),
]