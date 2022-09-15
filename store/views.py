from multiprocessing import context
from unicodedata import category
from django.shortcuts import render, get_object_or_404

from category.models import Category
from . models import Product

def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories)
        product_count = products.count()
    else:
        products = Product.objects.all()
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    single_product = Product.objects.get(category__slug=category_slug, slug=product_slug) # the double underscore means that we are getting the slug of the category of the product, i.e
    # the product(in its model) has a category, which is a foreign key from the category model, and the category model has its slug, and that is what we are getting
    # and after fetching it we match it to the category_slug that we are getting from the url
    # the category_slug and product_slug are from the url paths we created
    context = {
        'single_product': single_product,
    }
    return render(request, 'store/product_detail.html', context)
