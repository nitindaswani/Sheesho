from django.db import models
import uuid

# Create your models here.
 
class users(models.Model):
    user_id=models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    number=models.CharField(max_length=15)
    address=models.TextField()
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pincode=models.CharField(max_length=10)
    def __str__(self):
        return self.name