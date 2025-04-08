from django.shortcuts import render, redirect
from .models import Product
from .csv_parser import parse_rrc
from django.http import HttpResponse  # Додаємо імпорт
import requests
import xml.etree.ElementTree as ET

def index(request):
    """
    View function for the index page.
    """
    products = Product.objects.filter(provider="Tilly")
    context = {
        'products': products,
    }
    
    return render(request, 'index.html', context)

def xml_parsing(request):
    
    products = Product.objects.filter(provider="Tilly")
    url = "https://carrellobaby.com/uk_offers.xml"
    
    response = requests.get(url)
    response.raise_for_status() 
    root = ET.fromstring(response.content)
    offer_ids = [offer.get("id") for offer in root.findall(".//offer")]
    for offer_id in offer_ids:
        for product in products:
            if product.code == offer_id:
                product.status = True
                product.save()    
                break
        
                            
    
    return redirect('index')

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