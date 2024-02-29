from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Payment
from accounts.models import SubscriptionPlan, UserSubscription
from django_daraja.mpesa.core import MpesaClient


@login_required
def payment_page(request, subscription_id):
    subscription = UserSubscription.objects.get(id=subscription_id)
    return render(request, 'payments/payment_page.html', {'subscription': subscription})

@login_required
def process_payment(request):
    if request.method == 'POST':
        print(request.POST)
        subscription_id = request.POST.get('subscription_id')
        subscription_plan = SubscriptionPlan.objects.get(id=subscription_id)
      
        phone = request.POST.get('phone')
        cl = MpesaClient()
        phone_number = '0702239686'
        amount = int(subscription_plan.price)
        account_reference = 'reference'
        transaction_desc = 'Description'
        callback_url = 'https://api.darajambili.com/express-payment'
        response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
        return HttpResponse(response)
        # Process payment and update subscription status
        # Redirect to a confirmation page or dashboard
        # return redirect(reverse('subscription_confirmation'))
    # else:
        # Redirect to an error page or previous page

@login_required
def subscription_confirmation(request):
    return render(request, 'payments/subscription_confirmation.html')