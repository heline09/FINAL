from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import MpesaPayment
from accounts.models import SubscriptionPlan, UserSubscription, CustomUser
from django_daraja.mpesa.core import MpesaClient
import json
from .mpesa.core import verify_payment
from .mpesa.status import MpesaStatus
from datetime import timedelta, datetime
from django.views.decorators.csrf import csrf_exempt




@login_required
def payment_page(request, plan_id):
    subscription = SubscriptionPlan.objects.get(id=plan_id)
    return render(request, 'payments/payment_page.html', {'subscription': subscription})

@login_required
def process_payment(request):
    BASE_URL = 'https://e7e2-62-8-66-216.ngrok-free.app/'

    if request.method == 'POST':
        plan_id = request.POST.get('subscription_id')
        subscription_plan = SubscriptionPlan.objects.get(id=plan_id)
        user_id = request.user.id

        phone = request.POST.get('phone')
        cl = MpesaClient()
        amount = 1 #int(subscription_plan.price) 
        account_reference = 'reference'
        transaction_desc = 'Description'
        callback_url = BASE_URL+ f'payments/call_back_url/{user_id}/{plan_id}/'
        
        response = cl.stk_push(phone, amount, account_reference, transaction_desc, callback_url)
      
        if response.response_code == "0":
            return redirect('confirm_payment', plan_id)
        else:
            messages.error(request, "We couldn't process your payment")
            return redirect('payment_page', plan_id)
        
        
@csrf_exempt
def call_back_url(request, user_id, plan_id):
    """
    Mpesa will send the data to this URL upon payment / cancellation
    """
    print('call_back_url')
    if request.method == 'POST':
        results = MpesaClient().parse_stk_result(request.body)
        print(results)
        result_code = results.get("ResultCode") # type -> Int
        print(result_code)
        transaction_date = results.get("TransactionDate")  # Transaction date/time
        amount = results.get("Amount")
        receipt_number = results.get('MpesaReceiptNumber') # remember to add this to model and makemigrations 

        if result_code == 0: 
           print(result)
           user = CustomUser.objects.get(id=user_id)
           subscription = SubscriptionPlan.objects.get(id=plan_id)
           MpesaPayment.objects.create(user=user, amount=amount, subscription=subscription, is_complete=True, reference_id=receipt_number)
        return JsonResponse(data={'status':200}, status=200)

    else:   
        return HttpResponse("Invalid request method", status=405)          


def confirm_payment(request, plan_id):
    """
    Ask the user if they have paid then check the database to verify 
    """
    mpesa_payment = MpesaPayment.objects.filter(user=request.user, subscription_id=plan_id)
    print(mpesa_payment)
    if request.method=='POST':
        if mpesa_payment.exists():

            messages.success(request, 'Payment was successful')
            return redirect('recruiter_dashboard')
        else:
            messages.error(request, 'Payment does not exist')
            return redirect('payment_page', plan_id)
            
    context = {'plan_id': plan_id}
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
 