from django.db import models
from django.core.validators import MinValueValidator, EmailValidator

class products(models.Model):
    pro_id = models.AutoField(primary_key=True)
    pro_name = models.CharField(max_length=100)
    pro_desc = models.TextField()
    pro_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    pro_image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Products"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.pro_name} - ${self.pro_price}"

class orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, validators=[EmailValidator()])
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    ord_pro_id = models.IntegerField(null=True)
    ord_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    ord_pro_name = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Orders"
        ordering = ['-created_at']

    def __str__(self):
        return f"Order #{self.order_id} - {self.name} - {self.ord_pro_name}"