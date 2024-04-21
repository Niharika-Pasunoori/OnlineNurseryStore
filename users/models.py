from django.db import models
import uuid
from products.models import Product
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phone=models.CharField(max_length=20,null=True)
    address=models.CharField(max_length=200,null=True)

    REQUIRED_FIELDS = ['phone', 'address']

    


class Order(models.Model):
    STATUS=(
        ('Pending','pending'),
        ('Out for delivery', 'out for devilvery'),
        ('Delivered','delivered')
    )
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    status=models.CharField(max_length=200,null=True,blank=True,choices=STATUS)
    in_cart=models.BooleanField(default=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=True)
    def __str__(self):
        return str(self.product)
    
    @property
    def get_cost(self):
        cost = self.product.price
        total_sum = self.quantity * cost
        return total_sum
