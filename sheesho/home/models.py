from django.db import models

from products.models import products
from register.models import users


# Create your models here.

class Review(models.Model):
    product = models.ForeignKey(products, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(users, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.name} - {self.product.pro_name}"