from django.shortcuts import render , get_object_or_404 , HttpResponse
from . models import product , Category


# Create your views here.
def store(request , category_slug=None):
    category = None
    products = None 

    if category_slug != None:
        category = get_object_or_404(Category , category_slug=category_slug)
        products = product.objects.filter(category_fk=category , is_available=True)
        # print(products)
        product_count = products.count()

    else:
        products = product.objects.all().filter(is_available=True)
        # print(products)   
        product_count = products.count()
    
    context = {
        'product': products,
        'products_count': product_count
    }

    return render(request , "store/store.html" , context = context) 


def product_details(request , category_slug , product_slug):

    # print("functionsssssssss callinggggg" , category_slug , product_slug )
    try : 
        single_product = product.objects.get(
                category_fk__category_slug = category_slug,
                product_slug = product_slug
            )
                
    except product.DoesNotExist:
        single_product = None
        # print("Product not found")
        raise HttpResponse("Product not found")
    
    context = {
        'single_product': single_product,
        # 'products_count': product_count
    }
    

    return render(request , "store/product_details.html" , context = context)