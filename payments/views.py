from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Payment
from accounts.models import SubscriptionPlan, UserSubscription
from django_daraja.mpesa.core import MpesaClient
import json


@login_required
def payment_page(request, plan_id):
    subscription = SubscriptionPlan.objects.get(id=plan_id)
    return render(request, 'payments/payment_page.html', {'subscription': subscription})

@login_required
def process_payment(request):
    BASE_URL = 'https://13f0-102-219-210-201.ngrok-free.app'

    if request.method == 'POST':
        plan_id = request.POST.get('subscription_id')
        subscription_plan = SubscriptionPlan.objects.get(id=plan_id)
        user_id = request.user.id

        phone = request.POST.get('phone')
        cl = MpesaClient()
        amount = int(subscription_plan.price)
        account_reference = 'reference'
        transaction_desc = 'Description'
        callback_url = BASE_URL + f'/subscription_confirmation/{user_id}/{plan_id}/'
        
        response = cl.stk_push(phone, amount, account_reference, transaction_desc, callback_url)

        return HttpResponse(response)

        # Process payment and update subscription status
        # Redirect to a confirmation page or dashboard
        # return redirect(reverse('subscription_confirmation'))
    # else:
        # Redirect to an error page or previous page


def subscription_confirmation(request, user_id, plan_id):
    """
    Mpesa will send the data to this URL upon payment / cancellation
    """

    if request.method == 'POST':
        body = json.loads(request.body)
        results = body.get("Body", {}).get("stkCallback", {})
        result_code = results.get("ResultCode")  # type -> Int

        print(results)
    return render(request, 'payments/subscription_confirmation.html')


def confirm_payment(request):
    """
    Ask the user if they have paid then check the database to verify 
    """
    if request.method == 'POST':
         # user has selected 'Yes I've Paid'
        # Fetch the UserSubscription for request.user and plan_id
        pass
    return render(request, 'payments/confirm_payment.html')
