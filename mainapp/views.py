import json

from django.shortcuts import render
from mainapp.models import Product as P, ProductCategory as PS


# Create your views here.
def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context=context)


def products(request):

    #
    category = PS.objects.all()
    products = P.objects.all()
    context = {'title': 'GeekShop-каталог', 'category': category, 'products':products}
    return render(request, 'mainapp/products.html', context=context)


