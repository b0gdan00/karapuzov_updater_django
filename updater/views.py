from django.shortcuts import render
from .models import Product


def index(request):
    """
    View function for the index page.
    """
    products = Product.objects.filter(provider="Tilly")
    context = {
        'products': products,
    }
    
    return render(request, 'index.html', context)
