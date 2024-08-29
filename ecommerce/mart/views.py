# from django.shortcuts import render
# from django.http import HttpResponse
# from django.utils.http import urlencode

# # Create your views here.
# def index(request):
#     # return HttpResponse("<h1> This is mart <h1/>")
#     # varname = "Moataz"
#     # varname2 = ["Moataz", "Sobhy", "Zaki"]
#     # varname3 = {"Glasses":150, "Paper":110, "Scissors": 210}
#     # varname4 = {
#     #     "Glasses": {"price": 150, "image_url": "https://m.media-amazon.com/images/I/31QPu+05EaL._AC_SY580_.jpg"},
#     #     "Paper": {"price": 110, "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSF2m7CWtSAkz8qzir-kHKgjG_GkfAfnbGFSQ&s"},
#     #     "Scissors": {"price": 210, "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT30gTJwD7UdsQCeU1F1hNKM7Soymu5PI65lQ&s"},
#     # }
#     products = {"Glasese": 550, "Paper": 110, "Scissors": 230}
#     if request.method == "POST":
#         # print(request.POST) 
#         selected_items = request.POST.getlist("options")
#         print(selected_items)
#         base_url = "/show/"
#         query_string = urlencode({"options": selected_items})
#         url = f"{base_url}?{query_string}" 
#         return HttpResponse(url)
#     # return render(request, "mart/index.html", {"name":varname})
#     # return render(request, "mart/index.html", {"namelist":varname2})
#     # return render(request, "mart/index.html", {"namedic":varname3})
#     # return render(request, "mart/index.html", {"namedic2":varname4})
#     return render(request, "mart/index.html", {"namedic3":products})

# def show(request):
#     selected_options = request.GET.getlist("options")
#     render(request, "mart/show.html", {"products": selected_options})

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.http import urlencode
from products.models import Product  # Import from the correct app

def index(request):
    # Query all active products from the database
    products = Product.objects.filter(active=True)
    
    if request.method == "POST":
        # Get selected product names from the form submission
        selected_items = request.POST.getlist("options")
        print(selected_items)
        base_url = "/show/"
        query_string = urlencode({"options": selected_items})
        url = f"{base_url}?{query_string}" 
        return HttpResponse(url)

    # Pass the products to the template
    return render(request, "mart/index.html", {"products": products})

def show(request):
    selected_options = request.GET.getlist("options")
    
    # Query the selected products based on the selected names
    selected_products = Product.objects.filter(name__in=selected_options)
    
    return render(request, "mart/show.html", {"products": selected_products})
