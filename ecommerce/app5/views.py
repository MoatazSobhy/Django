from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def login(request):
    if request.method == "POST":
        # username = request.POST.get('Username')
        # password = request.POST.get('Password')
        # a = Login(username=username, password=password)
        # a.save()
        # print(request.POST)
        
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # b = Login(username= username, password= password)
        # b.save()
        
        c = LoginForm(request.POST)
        c.save()
    return render(request, 'app5/login.html', {'lf': LoginForm })