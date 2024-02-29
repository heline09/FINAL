from django.urls import path, include
from . import views


urlpatterns = [
    path('signin/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('skills/', views.skillPage, name="skills"),
    path('logout/',views.logoutUser, name="logout"),
    path('subscribe/', views.subscribePage, name = "subscribePage"),
    # path('subscription/choose/<int:plan_id>/', views.choose_subscription, name="choose_subscription"),
    path('subscription/user/', views.user_subscriptions, name="user_subscriptions"),
]