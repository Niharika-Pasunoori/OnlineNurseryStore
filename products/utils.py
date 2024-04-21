from .models import Product,Category
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def paginationProducts(request,products,results):
    
    page=request.GET.get('page')
    results=3
    paginator=Paginator(products,results)
    try:
        products=paginator.page(page)
    except PageNotAnInteger:
        page=1
        products=paginator.page(page)
    except EmptyPage:
        page=paginator.num_pages # last page
        products=paginator.page(page)

    leftIndex=(int(page) - 1)

    if leftIndex < 1:
        leftIndex=1
    
    rightIndex=(int(page) + 1)

    if rightIndex > paginator.num_pages:
        rightIndex=paginator.num_pages+1

    custom_range=range(leftIndex,rightIndex)

    return custom_range,products


def searchProducts(request):
    search_query=''

    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')
    
    # print('SEARCH:', search_query)
    products=Product.objects.distinct().filter(Q(name__icontains=search_query) | Q(category__name__icontains=search_query) | Q(placement__icontains=search_query))

    return products,search_query