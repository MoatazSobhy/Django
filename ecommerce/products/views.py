from django.shortcuts import render

# Create your views here.
def product(request):
    return render(request, "products/product.html")

def products(request):
    return render(request, "products/products.html")