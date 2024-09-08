from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("<h1>index page</h1>")
    x = {"name":"Moataz Sobhy Zaki", "age":2727272727}
    return render(request, template_name='app1/index.html',context=x)


def about(request):
    # return HttpResponse("<h1>about page</h1>")
    return render(request, template_name='app1/about.html')