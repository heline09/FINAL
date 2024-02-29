from django.db import models
from accounts.models import CustomUser, SubscriptionPlan

class Payment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default="USD")
    payment_method = models.CharField(max_length=255, choices=[("credit_card", "Credit Card"), ("debit_card", "Debit Card"), ("bank_transfer", "Bank Transfer")])
    transaction_id = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=255, choices=[("pending", "Pending"), ("completed", "Completed"), ("failed", "Failed")])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
