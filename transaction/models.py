from django.db import models
import uuid
# Create your models here.
class Transaction(models.Model):
    payment = models.OneToOneField('payment.Payment', on_delete=models.PROTECT , related_name='transaction')   # P for model and p for app
    reference = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)