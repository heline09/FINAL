from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import MpesaPayment
from accounts.models import SubscriptionPlan, UserSubscription
from django_daraja.mpesa.core import MpesaClient
import json
from .mpesa.core import verify_payment
from .mpesa.status import MpesaStatus
from datetime import timedelta, datetime


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
        print(f'The response code is:{response.response_code}')
        if response.response_code == "0":
            mpesa_payment = MpesaPayment.objects.create(user=request.user, subscription=subscription_plan, reference_id=response.checkout_request_id)
            return redirect('confirm_payment', mpesa_payment.id)
        else:
            messages.error(request, "We couldn't process your payment")
            return redirect('payment_page', plan_id)
        
        

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


def confirm_payment(request, mpesa_payment_id):
    """
    Ask the user if they have paid then check the database to verify 
    """
    context = {'mpesa_payment_id':mpesa_payment_id}
    return render(request, 'payments/confirm_payment.html', context)
   
def MpesaPaymentConfirmation(request,mpesa_payment_id):
    """
    Ask the user if they have paid then check the database to verify 
    """ 
    mpesa_payment = get_object_or_404(MpesaPayment, id = mpesa_payment_id)
    if mpesa_payment.is_complete:
        messages.error(request, 'You have already paid')
        return redirect('recruiter_dashboard')
    payement_status =  verify_payment(mpesa_payment.reference_id)
    print(payement_status)
    if payement_status == MpesaStatus.Completed:
        end_date = datetime.now()+timedelta(days=mpesa_payment.subscription.duration)
        user_subscription = UserSubscription.objects.create(plan=mpesa_payment.subscription, user=mpesa_payment.user, active=True, end_date=end_date)
        request.user.subscription_plan = mpesa_payment.subscription
        request.user.save()
        mpesa_payment.is_complete = True
        mpesa_payment.save()
        messages.success(request, 'Payment was successful')
        return redirect('recruiter_dashboard')
    else:
        messages.error(request, 'Payment was not successful.Try again')
        return redirect('payment_page', mpesa_payment.subscription.id)
 