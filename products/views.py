from django.shortcuts import render,get_object_or_404, redirect
from .models import Product,Category
from users.models import Order
from .forms import AddProductForm,UpdateOrderForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from users.decorators import admin_only
from .utils import searchProducts,paginationProducts

# Create your views here.

def home(request):
    categoryList=Category.objects.all()
    context={'categoryList':categoryList}
    return render(request,'landingPage.html',context)


def productsList(request,pk=None):
    category=Category.objects.get(id=pk)
    productList=category.product_set.all()
    context={'productList':productList,'category':category}
    return render(request,'products/target-product.html',context)

def products(request):
    # products=Product.objects.all()
    products,search_query=searchProducts(request)
    custom_range,products=paginationProducts(request,products,4)
    # print(custom_range)
    context={'products':products,'search_query':search_query,'custom_range':custom_range}
    return render(request,'products/products.html',context)

def productDetail(request,pk=None): 
    product=Product.objects.get(id=pk)
    context={'product':product}
    return render(request,'products/productDetails.html',context)

@login_required(login_url='loginUser')
@admin_only
def addProduct(request):
    form=AddProductForm()
    if request.method=='POST':
        form=AddProductForm(request.POST,request.FILES)
        if form.is_valid():
            product=form.save()
            messages.success(request,'Product is addedd Successfully')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
            messages.warning(request,'An error has occured, please add again')
    context={'form':form}
    return render(request,'products/add-product.html',context)

@login_required(login_url='loginUser')
@admin_only
def admin_products_page(request):
    products=Product.objects.all()
    custom_range,products=paginationProducts(request,products,6)
    context={'products':products,'custom_range':custom_range}
    return render(request,'admin-products-page.html',context)

@login_required(login_url='loginUser')
@admin_only
def admin_orders_page(request):
    orders=Order.objects.all()
    custom_range,orders=paginationProducts(request,orders,6)
    context={'orders':orders,'custom_range':custom_range}
    return render(request,'admin-orders-page.html',context)

@login_required(login_url='loginUser')
@admin_only
def delete_product(request, pk=None):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully')
    else:
        messages.warning(request, 'Something went wrong, try again...!')
    return redirect(reverse('admin_products_page'))

@login_required(login_url='loginUser')
@admin_only
def delete_order(request, pk=None):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        messages.success(request, 'Order deleted successfully')
    else:
        messages.warning(request, 'Something went wrong, try again...!')
    return redirect(reverse('admin_orders_page'))

@login_required(login_url='loginUser')
@admin_only
def update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = AddProductForm(instance=product)
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product=form.save(commit=False)
            product.save()
            messages.success(request, 'Changes are updated successfully!!')
        else:
            messages.warning(request, 'An error has occurred while saving the changes')
    
    return render(request, 'products/update-product.html', {'form': form, 'product': product})

@login_required(login_url='loginUser')
@admin_only
def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = UpdateOrderForm(instance=order)
    if request.method == 'POST':
        form = UpdateOrderForm(request.POST, instance=order)
        if form.is_valid():
            order=form.save(commit=False)
            order.save()
            messages.success(request, 'Changes are updated successfully!!')
        else:
            messages.warning(request, 'An error has occurred while saving the changes')
    
    return render(request, 'products/update-order.html', {'form': form,'order':order})