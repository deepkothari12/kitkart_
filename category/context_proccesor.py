##used to list the all categories in the base.html file
from . models import Category
from store.models import product


def list_category(request):
    category_link = Category.objects.all()
    # print("_->", category_link)
    context = {
        'category': category_link
    }
    return context


def list_product(request):
    product_link = product.objects.all()
    # print("_->", category_link)
    context = {
        'product': product_link
    }
    return context