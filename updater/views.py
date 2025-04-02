from django.shortcuts import render, redirect
from .models import Product
from .csv_parser import parse_rrc
from django.http import HttpResponse  # Додаємо імпорт


def index(request):
    """
    View function for the index page.
    """
    products = Product.objects.filter(provider="Tilly")
    context = {
        'products': products,
    }
    
    return render(request, 'index.html', context)

def upload_csv(request):
    if request.method == "POST" and request.FILES.get("file"):
        uploaded_file = request.FILES["file"]
        parsed_data = parse_rrc(uploaded_file)  # Парсимо CSV

        for item in parsed_data:
            sku = item.get("sku")
            price = item.get("price_rrc")
            code = item.get("code")

            Product.objects.update_or_create(
                sku=sku,
                defaults={"price": price.replace(",", "."), "code": code, "provider": "Tilly", "status": False}
            )


    return redirect('index')