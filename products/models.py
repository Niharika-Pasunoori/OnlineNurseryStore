from django.db import models
import uuid


class Category(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    name = models.CharField(max_length=20)
    category_image = models.ImageField(upload_to ='products/',null=True)
    caption= models.CharField(max_length = 200, default = "", null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 50)
    price = models.IntegerField(default = 0)
    category = models.ForeignKey(Category , on_delete=models.CASCADE, default=1)
    placement=models.CharField(max_length = 200, default = "", null=True, blank=True)
    description = models.CharField(max_length = 200, default = "", null=True, blank=True)
    image = models.ImageField(upload_to ='products/')
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.name