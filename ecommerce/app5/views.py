from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import TemplateView
from django.http import HttpResponse

# # Create your views here.
# def login(request):
#     if request.method == "POST":
#         # username = request.POST.get('Username')
#         # password = request.POST.get('Password')
#         # a = Login(username=username, password=password)
#         # a.save()
#         # print(request.POST)
        
#         # username = request.POST.get('username')
#         # password = request.POST.get('password')
#         # b = Login(username= username, password= password)
#         # b.save()
        
#         c = LoginForm(request.POST)
#         c.save()
#     return render(request, 'app5/login.html', {'lf': LoginForm })


class cbv(TemplateView):
    template_name = 'app5/cbv.html'
    def get(self, request):
        response = HttpResponse("<h1>Hello from cbv</h1>")
        return
    def post():
        pass
    