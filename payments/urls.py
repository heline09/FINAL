from django.urls import path, include
from . import views

urlpatterns = [
    # Other URL patterns
    path('payment/<int:plan_id>/', views.payment_page, name='payment_page'),  
    path('process_payment/', views.process_payment, name='process_payment'), 
    path('subscription_confirmation/<int:user_id>/<int:plan_id>/', views.subscription_confirmation, name='subscription_confirmation'),  
    path('confirm_payment/', views.confirm_payment, name='confirm_payment'),
]