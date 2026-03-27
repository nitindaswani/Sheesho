from django.db import models
import uuid
from django.core.validators import RegexValidator


# Create your models here.

phone_validator = RegexValidator(
    regex=r'^\d{10}$',
    message="Phone number must be exactly 10 digits."
)

class orders(models.Model):
    order_id=models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    ord_date= models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        default="pending"
    )
    user_id=models.UUIDField(null=True, blank=True)
    
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=100)
    phone=models.CharField(max_length=10,validators=[phone_validator])
    
    
    ord_pro_id=models.UUIDField(null=True)
    ord_price=models.FloatField(null=True)
    ord_pro_name=models.CharField(max_length=100,null=True)