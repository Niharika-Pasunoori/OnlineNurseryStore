from django.urls import path
from .import views

urlpatterns=[
    path('register/',views.registerUser,name="register"),
    path('login/',views.loginUser,name="loginUser"),
    path('logout/',views.logoutUser,name="logoutUser"),
    path('userProfile/',views.userProfile,name="userProfile"),
    path('orders/',views.viewOrders,name="viewOrders"),
    path('cart/',views.viewCart,name="viewCart"),
    path('update_item/',views.updateItem,name="update_item"),
    path('checkout/',views.checkout,name="checkout"),
    path('process_order/',views.processOrder,name="process_order"),
    # path('admin-page/',views.adminPage,name="adminPage"),
]