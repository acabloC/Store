from django.shortcuts import render
from .models import *
def index(request):
    context={"name":"Магазинус"}

    return render(request, 'index.html',context=context)

def products(request):
    context = {
          "title": "Магазинус-каталог",
          "products":Product.objects.all(),
          "category":ProductCategory.objects.all()}


    return render(request, 'products.html', context = context)