from django.db import models
import uuid

# Create your models here.

class products(models.Model):
    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('fashion', 'Fashion'),
        ('footwear', 'Footwear'),
        ('home-kitchen', 'Home & Kitchen'),
        ('beauty', 'Beauty'),
        ('grocery', 'Grocery'),
        ('books', 'Books'),
        ('sports', 'Sports'),
        ('toys-baby', 'Toys & Baby'),
        ('automotive', 'Automotive'),
        ('jewellery', 'Jewellery'),
        ('accessories', 'Accessories'),
    ]
    
    
    
    pro_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    pro_name=models.CharField(max_length=100)
    pro_desc=models.TextField()
    pro_price=models.FloatField()
    pro_category=models.CharField(max_length=50,choices=CATEGORY_CHOICES)
    pro_stock=models.IntegerField(default=0)
    pro_image=models.ImageField(upload_to='products/')
    
    def __str__(self):
        return self.pro_name