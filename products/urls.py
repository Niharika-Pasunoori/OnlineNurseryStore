from django.urls import path
from .import views

urlpatterns = [ 
     path('',views.home,name='home'), 
    path('category/<str:pk>',views.productsList,name='productsList'),
    path('product/<str:pk>',views.productDetail,name='productDetail'),
    path('products',views.products,name='products'),
    path('add-product/',views.addProduct,name='addProduct'),
    path('admin-products-page/',views.admin_products_page,name='admin_products_page'),
    path('admin-orders-page/',views.admin_orders_page,name='admin_orders_page'),
    path('product-delete/<str:pk>/', views.delete_product, name='delete_product'),
    path('order-delete/<str:pk>/', views.delete_order, name='delete_order'),
    path('update-product/<str:pk>/', views.update_product, name='update_product'),
    path('update-order/<str:pk>/', views.update_order, name='update_order'),
]
