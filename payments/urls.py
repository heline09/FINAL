from django.urls import path, include
from . import views

urlpatterns = [
    # Other URL patterns
    path('payment/<int:subscription_id>/', views.payment_page, name='payment_page'),  
    path('process-payment/', views.process_payment, name='process_payment'), 
    path('subscription-confirmation/', views.subscription_confirmation, name='subscription_confirmation'),  
]