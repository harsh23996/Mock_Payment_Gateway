from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Payment(models.Model):    
    receiver = models.ForeignKey(User, on_delete=models.PROTECT, related_name='received_payments')
    sender = models.ForeignKey(User, on_delete=models.PROTECT, related_name='sent_payments')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, default = "pending")
    created_at = models.DateTimeField(auto_now_add=True)