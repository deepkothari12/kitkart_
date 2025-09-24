from django.http import HttpResponse
from django.shortcuts import render
from store.models import product

def main_view(request):
    products = product.objects.all().filter(is_available=True)
    # print(products)
    context = {
        'product': products
    }


    return render(request, "index.html" , context=context)