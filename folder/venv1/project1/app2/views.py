from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def index2(request):
    return HttpResponse("<h1>Hello from second app</h1>")

def product(request):
    return render(request, 'app2/index22.html' )

def products(request):
    return render(request, 'app2/index2.html', {'pro':Product.objects.all()})
    # return render(request, 'app2/index2.html', {'pro':Product.objects.all().filter(name = 'Tesla Car')})
    # return render(request, 'app2/index2.html', {'pro':Product.objects.all().order_by('price')})
    # return render(request, 'app2/index2.html', {'pro':str(Product.objects.all().count())})
    # return render(request, 'app2/index2.html', {'pro':Product.objects.all().exclude(price = 2000)})
    # return render(request, 'app2/index2.html', {'pro':Product.objects.all().filter(price__exact = 2000)})
    # return render(request, 'app2/index2.html', {'pro':Product.objects.all().filter(name__contains = 'Lap')})
    # return render(request, 'app2/index2.html', {'pro':Product.objects.all().filter(price__in = [2000,5000])})
    # return render(request, 'app2/index2.html', {'pro':Product.objects.all().filter(price__range =(2000,6000))})
    
