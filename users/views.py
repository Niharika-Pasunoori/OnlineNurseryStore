from django.shortcuts import render,redirect,get_object_or_404
from .forms import CustomUserCreationForm,UserProfileForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order
from products.models import Product
from .decorators import unauthenticated_user,allowed_users
from django.http import JsonResponse
import json


User=get_user_model()

@login_required(login_url='loginUser')
@allowed_users(allowed_roles=['customers'])
def userProfile(request):
    
    edit_mode = request.GET.get('edit', False)
    profile=request.user
    form=UserProfileForm(instance=profile)
    if request.method=='POST':
        form=UserProfileForm(request.POST,instance=profile)
        if form.is_valid():
            user=form.save()
            messages.success(request,'Changes are updated successfuly!!')
            return redirect('home')
        else:
            messages.warning(request,'An error has occured while saving the changes')

    context={'form': form,'edit_mode': edit_mode}
    return render(request,'users/user_profile.html',context)

@unauthenticated_user
def loginUser(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        try:
            user=User.objects.get(username=username)
        except:
            messages.warning(request,"Username doesnot exist")

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request,"Username or password is incorrect")

    return render(request, 'users/user_register.html')  


def logoutUser(request):
    logout(request)
    messages.info(request,"User logged out!!")
    return redirect('loginUser')

@unauthenticated_user
def registerUser(request):
    page='register'
    form=CustomUserCreationForm()

    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.usernmae=user.username.lower()
            user.save()

            customers_group = Group.objects.get(name='customers')
            user.groups.add(customers_group)

            messages.success(request,'User account is created')
            login(request,user)
            return redirect('home')

        else:
            messages.warning(request,'An error has occured during registration')
    context={'form':form,'page':page}
    return render(request,'users/user_register.html',context)

@login_required(login_url='loginUser')
@allowed_users(allowed_roles=['customers'])
def viewCart(request):
    orderDetails = Order.objects.filter(user=request.user, in_cart=True)
    total_cost = sum(order.get_cost for order in orderDetails)
    context={'orderDetails': orderDetails, 'total_cost': total_cost}
    return render(request, 'users/cart.html', context)

def updateItem(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']

    print('Action:',action)
    print('productId:',productId)

    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        product=product,
        user=request.user,
        status='Pending',
        in_cart=True  # Assuming newly added items are pending by default
    )
    if action == 'add':
        order.quantity += 1
    elif action == 'remove':
        order.quantity -= 1
    order.save()

    if order.quantity <= 0: 
        order.delete()
    
    return JsonResponse('Item was added', safe=False)

@login_required(login_url='loginUser')
@allowed_users(allowed_roles=['customers'])
def checkout(request, product_id=None):
    #    order,created=Order.objects.get_or_create(customer=customer,complete=False)
    orderDetails=Order.objects.filter(user=request.user,in_cart=True)
    total_sum = sum(order.get_cost for order in orderDetails)
    total_items=sum([item.quantity for item in orderDetails])

    profile=request.user
    form=UserProfileForm(instance=profile)
    if request.method=='POST':
        form=UserProfileForm(request.POST,instance=profile)
        if form.is_valid():
            user=form.save()
        
    context={'orderDetails':orderDetails,'total_sum':total_sum,'total_items':total_items,'form':form}
    return render(request, 'users/checkout.html', context)

@login_required(login_url='loginUser')
@allowed_users(allowed_roles=['customers'])
def processOrder(request):
    orderDetails=Order.objects.filter(user=request.user,in_cart=True)
    for order in orderDetails:
         order.in_cart=False 
         order.save()
    return JsonResponse('Payment Complate',safe=False)

@login_required(login_url='loginUser')
@allowed_users(allowed_roles=['customers'])
def viewOrders(request):
    orderDetails=Order.objects.filter(user=request.user,in_cart=False)
    sum=0
    for order in orderDetails:
        sum+=order.get_cost
    # product=orderDetails.product_set.all()
    context={'orderDetails':orderDetails,'sum':sum}
    return render(request,'users/orders_page.html',context)

 

