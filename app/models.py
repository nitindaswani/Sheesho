from django.db import models

# Create your models here.

class products(models.Model):
    pro_id=models.AutoField(primary_key=True)
    pro_name=models.CharField(max_length=100)
    pro_desc=models.TextField()
    pro_price=models.FloatField()
    pro_image=models.ImageField(upload_to='images')
    
class orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    ord_pro_id=models.IntegerField(null=True)
    ord_price=models.FloatField(null=True)
    ord_pro_name=models.CharField(max_length=100,null=True)