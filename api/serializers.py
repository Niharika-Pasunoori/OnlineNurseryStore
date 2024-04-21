from rest_framework import serializers
from products.models import Product,Category
from users.models import Order,CustomUser

class CategorySerilaizer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'


class ProductSerilaizer(serializers.ModelSerializer):
    category=CategorySerilaizer(many=False)
    class Meta:
        model=Product
        fields='__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'