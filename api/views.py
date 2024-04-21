from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import ProductSerilaizer,OrderSerializer
from products.models import Product
from users.models import Order

@api_view(['GET'])
def getRoutes(request):

    routes=[
        {'GET':'/api/products'},
        {'GET':'/api/product/id'},
        {'PUT':'api/product/id'},
        {'GET':'/api/orders'},
        {'GET':'api/order/id'},
        {'PUT':'api/order/id'}
    ]

    return Response(routes)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProducts(request):
    products=Product.objects.all()
    serializer=ProductSerilaizer(products,many=True).data
    return Response(serializer)

@api_view(['GET'])
def getProduct(request,pk):
    product=Product.objects.get(id=pk)
    serializer=ProductSerilaizer(product,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getOrders(request):
    orders=Order.objects.all()
    serializer=OrderSerializer(orders,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getOrder(request,pk):
    order=Order.objects.get(id=pk)
    serializer=OrderSerializer(order,many=False)
    return Response(serializer.data)
